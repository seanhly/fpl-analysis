#!/usr/bin/bash
duckdb <<<"copy (
	with x as (
		select player_id, lower(name) team, position, lower(second_name || ' ' || first_name) player, cost from 'data/parsed/players.csv' natural join 'data/parsed/teams.csv'
	),
	y as (
		select player_id, sum(predicted_pts) predicted_pts from 'data/parsed/predictions.csv' group by player_id
	)
	select "'*'" exclude predicted_pts from x natural join y order by team, position, predicted_pts desc
) to 'sources/fpl.players.tsv' with (header false,delimiter '\t');"

#(cd sources/fpl.team && for f in $(seq 1 752); do
#	curl https://fpl.team/players/$f/ > $f.html
#done)

(cd sources/fpl.team &&
echo -e "player\tteam\tposition\tcost\tgw+1\tgw+2\tgw+3" &&
for f in *.html; do
	echo -e "$(
		grep -A1 '<div class="player-title"' $f |
			cut -d'>' -f2 |
			cut -d'<' -f1 |
			paste -sd$'\t' |
			sed 's| / |\t|g' |
			sed "s|\&\#39\;|'|g"
	)\t$(
		grep -Eo 'Price <span class="badge">[0-9.]+</span>' $f |
			cut -d'>' -f2 |
			cut -d'<' -f1
	)\t$(
		grep '>xPts<' -A1 $f |
			awk 'NR%3==2{print}' |
			cut -d'>' -f2 |
			cut -d'<' -f1 |
			paste -sd$'\t'
	)"
done) | awk -F$'\t' '{
	print tolower($2) FS $3 FS tolower($1) FS $4 FS $5 FS $6 FS $7
}' > sources/fpl.team.points.tsv
duckdb <<<"
copy (
	with x as (select team, position, player, cost, "'"'"gw+1"'"'" + "'"'"gw+2"'"'" + "'"'"gw+3"'"'" as predicted_points from 'sources/fpl.team.points.tsv')
	select "'*'" exclude predicted_points from x order by team, position, predicted_points desc
) to 'sources/fpl.team.players.tsv' with (header false, delimiter '\t');"
python coalescers/fpl.team.py > sources/fpl.team.mapping.tsv
duckdb <<<"copy(
	select
		player_id, "'*'" exclude (player, player_id, team, position, cost)
	from 'sources/fpl.team.points.tsv' fplteam
	natural join 'sources/fpl.team.mapping.tsv'
) to 'sources/fpl.team.tsv' (HEADER, DELIMITER '\\t');"
rm sources/fpl.team.points.tsv sources/fpl.team.mapping.tsv sources/fpl.team.players.tsv sources/fpl.players.tsv
(
	echo -e "player_id\tgameweek\tpredicted_points"
	tail -n+2 sources/fpl.team.tsv |
		awk -v CURRENT_GW=12 '{for(i=2;i<=NF;++i){print $1"\t"(i-2+CURRENT_GW)"\t"$i}}'
) | sponge sources/fpl.team.tsv
