find data/parsed_1 data/parsed -type f -delete
(echo player_id,first_name,second_name,team_id,cost
	jq -r '.elements[]|[.code,.first_name,.second_name,.team,.now_cost/10]|@csv' < data/raw/players.json
) > data/parsed_1/players.csv
cat data/raw/predictions.json | jq -r '.[]|.code as $c|.data|.positionId as $p|.predictions|select(.!=null)|.[]|[$c,.gw,.xmins,.predicted_pts,$p]|@csv' > data/parsed_1/predictions.csv
(echo position,player_id
cat data/parsed_1/predictions.csv |
	awk -F, '{print $5 FS $1}' |
	uniq |
	sort -k1,1 |
	sed $'s/^1/GKP/g' |
	sed $'s/^2/DEF/g' |
	sed $'s/^3/MID/g' |
	sed $'s/^4/FWD/g'
) > data/parsed_1/positions.csv
duckdb -csv <<< "select player_id,position,first_name,second_name,team_id,cost from 'data/parsed_1/players.csv' natural join 'data/parsed_1/positions.csv' order by cost desc;" > data/parsed/players.csv
(echo player_id,gameweek,predicted_mins,predicted_pts && cut -d, -f1-4 data/parsed_1/predictions.csv) > data/parsed/predictions.csv
(echo team_id,name && jq -r '.teams[]|[.id,.name]|@csv' < data/raw/players.json) > data/parsed/teams.csv
