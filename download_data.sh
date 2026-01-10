if [ -e data ]; then
	find -maxdepth 1 -regex '\./data[0-9]*' | sort -n -r | while read d; do
		digit="$(tr -d -c '[[:digit:]]' <<<$d)"
		if [ ! "$digit" ]; then digit=1; fi
		next=$((digit + 1))
		echo mv $d ./data$next
		mv $d ./data$next
	done
fi
cp -r data2 data
find data/raw -type f -delete
curl https://fantasy.premierleague.com/api/bootstrap-static/ > data/raw/players.json
curl https://www.fantasyfootballhub.co.uk/player-data/player-data.json > data/raw/predictions.json
