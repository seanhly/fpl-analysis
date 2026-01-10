 #!/usr/bin/bash
 cat sources/fplanalyser.com.html |
 	grep '<div id="app" data-page="' |
	cut -d'"' -f4 |
	sed -E 's/\&\#039\;/'"'"'/g' |
	sed 's/\&quot\;/"/g' |
	jq '.props.players.data' > \
	sources/fplanalyser.com.json

(
echo -e "player_id\tgameweek\tpredicted_minutes\tpredicted_points"
jq -r '.[]|.player_id as $p|.gameweekPredictions|to_entries[]|.key as $gw|.value|[$p,$gw,.minutes,.points]|@tsv' < \
	sources/fplanalyser.com.json |
	sed 's/\t$/\t0/g' |
	sort -n -t $'\t' -k 2,2 |
	sort -n -t $'\t' -k 1,1 --stable
) > sources/fplanalyser.com.tsv
