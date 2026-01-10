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

(jq '.[]|[.PlayerWebName,.TeamFullName,.PlayerPositionName,.Cost,(.UpcommingFixtures|[.[].ExpectedPoints])]' < \
	sources/fplgameweek.com.json) > sources/fplgameweek.com.min.json
jq -r '[add(.[4][]),.[1],.[2],.[0],.[3]]|@tsv' < sources/fplgameweek.com.min.json |
	sort -n -r |
	cut -d$'\t' -f2- |
	sort --stable -t$'\t' -k 1,2 |
	awk -F$'\t' '{
		print tolower($1) FS ($2 == "Defender" ? "DEF" : $2 == "Midfielder" ? "MID" : $2 == "Forward" ? "FWD" : "GKP") FS tolower($3) FS $4
	}' > sources/fplgameweek.players.tsv
jq -r '.[0] as $pl|.[1] as $t|.[2] as $po|.[3] as $c|.[4][]|[$t,$po,$pl,.,$c]|@tsv' < sources/fplgameweek.com.min.json |
	awk -F$'\t' 'BEGIN {
		print "team\tposition\tplayer\tn\tpredicted_points\tcost"
		POS["Defender"] = "DEF"
		POS["Goalkeeper"] = "GKP"
		POS["Midfielder"] = "MID"
		POS["Forward"] = "FWD"
	}
	{
		print tolower($1) FS POS[$2] FS tolower($3) FS NR FS $4 FS $5
	}' > sources/fplgameweek.points.tsv
python coalescers/fplgameweek.com.py > sources/fplgameweek.mapping.tsv

duckdb <<<"copy(
	select
		player_id,
		11 + dense_rank()over(partition by player_id order by n) gameweek,
		predicted_points
	from 'sources/fplgameweek.points.tsv'
	natural join 'sources/fplgameweek.mapping.tsv'
) to 'sources/fplgameweek.com.tsv' (HEADER, DELIMITER '\\t');"
rm sources/fplgameweek.points.tsv sources/fplgameweek.mapping.tsv sources/fplgameweek.com.min.json sources/fplgameweek.players.tsv sources/fpl.players.tsv
