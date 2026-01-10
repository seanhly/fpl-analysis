copy (
	select
		lower(Team) as team,
		replace(Position, 'GK', 'GKP') as position,
		lower(Name) as player,
		replace(replace(Price, 'm', ''), '£', '') as cost,
		cast(replace(Ownership, '%', '') as float) / 100 as owned_by,
		Predicted as "gw+1", GW2s as "gw+2", GW3s as "gw+3", GW4s as "gw+4", GW5s as "gw+5", GW6s as "gw+6"
	from 'sources/fantasyfootballpundit.com.csv' order by Team, Position, Predicted + GW2s + GW3s + GW4s + GW5s + GW6s desc
) to 'sources/fantasyfootballpundit.com.points.tsv' (HEADER, DELIMITER '\t');
