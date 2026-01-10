lookup='''
GKP.*Mamardashvi
GKP.*Dúbravka
DEF.*Gabriel..dos
DEF.*Timber
DEF.*Tosin
Chalobah
Mukiele
Miley
MID.*Isma.*Sarr
Saka
Szoboszlai
Haaland
Mateta
FWD.*Pedro
MID.*Borges Fernandes
'''
lookup=${lookup##[[:space:]]}
lookup=${lookup%%[[:space:]]}
team="$(cat data/parsed/players.csv | grep -E "$(paste -sd'|'<<<"${lookup}")")"
echo "$team" | grep ,GKP,
echo "$team" | grep ,DEF,
echo "$team" | grep ,MID,
echo "$team" | grep ,FWD,
