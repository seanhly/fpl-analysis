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
(
	echo -e "team\tposition\tplayer\tplayer_short\tcost\towned_by\tgameweek\tpredicted_points"
	(
		jq -r '.[]|.name as $n|.name_short as $ns|.pop as $pop|.pos as $pos|.team as $t|.value as $c|del(.name,.name_short,.person_id,.pop,.pos,.team,.team_short,.team_id,.value)|to_entries[]|[($t|ascii_downcase),$pos,($n|ascii_downcase),($ns|ascii_downcase),$c,$pop,.key,.value]|@tsv' < sources/managerbotten.dk.json
	) | sed -E 's/\tGK\t/\tGKP\t/g' 
) > sources/managerbotten.dk.points.tsv
duckdb <<<"
	copy (
		with x as (
			select team, position, player, player_short, cost, owned_by, sum(predicted_points) as predicted_points from 'sources/managerbotten.dk.points.tsv'
			group by team, position, player, player_short, cost, owned_by
		)
		select team, position, player, player_short, cost, owned_by from x
		order by team, position, predicted_points desc
	) to 'sources/managerbotten.dk.players.tsv' with (header false, delimiter '\t');
"
python coalescers/managerbotten.dk.py > sources/managerbotten.dk.mapping.tsv
duckdb <<<"copy(
	select
		player_id, "'*'" exclude (player, player_short, player_id, team, position, cost, owned_by)
	from 'sources/managerbotten.dk.points.tsv' pts
	natural join 'sources/managerbotten.dk.mapping.tsv'
) to 'sources/managerbotten.dk.tsv' (HEADER, DELIMITER '\\t');"
rm sources/managerbotten.dk.points.tsv sources/managerbotten.dk.mapping.tsv sources/managerbotten.dk.players.tsv sources/fpl.players.tsv
