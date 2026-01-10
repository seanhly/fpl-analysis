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

duckdb < coalescers/fantasyfootballpundit.com.sql
duckdb <<<"
copy (
	select "'*'"
	"' exclude ("gw+1", "gw+2", "gw+3", "gw+4", "gw+5", "gw+6")'"
	from 'sources/fantasyfootballpundit.com.points.tsv'
	order by team, position, "'"gw+1" + "gw+2" + "gw+3" + "gw+4" + "gw+5" + "gw+6"'" desc
) to 'sources/fantasyfootballpundit.com.players.tsv' with (header false, delimiter '\t')
;"
python coalescers/fantasyfootballpundit.com.py > sources/fantasyfootballpundit.com.mapping.tsv
duckdb <<<"copy(
	select
		player_id, "'*'" exclude (player, player_id, team, position, cost, owned_by)
	from 'sources/fantasyfootballpundit.com.points.tsv'
	natural join 'sources/fantasyfootballpundit.com.mapping.tsv'
) to 'sources/fantasyfootballpundit.com.tsv' (HEADER, DELIMITER '\\t');"
rm sources/fantasyfootballpundit.com.points.tsv sources/fantasyfootballpundit.com.mapping.tsv sources/fantasyfootballpundit.com.players.tsv sources/fpl.players.tsv
(
	echo -e "player_id\tgameweek\tpredicted_points"
	tail -n+2 sources/fantasyfootballpundit.com.tsv |
		awk -v CURRENT_GW=12 '{for(i=2;i<=NF;++i){print $1"\t"(i-2+CURRENT_GW)"\t"$i}}'
) | sponge sources/fantasyfootballpundit.com.tsv
