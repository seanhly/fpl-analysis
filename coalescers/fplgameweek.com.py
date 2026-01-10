#!/usr/bin/python
from unicodedata import normalize
import csv
from re import sub

fplgameweek = {}

with open("sources/fplgameweek.players.tsv", mode="r") as file:
    r = csv.reader(file, delimiter="\t")
    for team, position, player, cost in r:
        cost = float(cost)
        if team in fplgameweek:
            if position in fplgameweek[team]:
                fplgameweek[team][position].append((player, cost))
            else:
                fplgameweek[team][position] = [(player, cost)]
        else:
            fplgameweek[team] = {position: [(player, cost)]}

fpl = {}
with open("sources/fpl.players.tsv", mode="r") as file:
    r = csv.reader(file, delimiter="\t")
    for player_id, team, position, player, cost in r:
        player_id = int(player_id)
        cost = float(cost)
        if team in fpl:
            if position in fpl[team]:
                fpl[team][position].append((player_id, player, cost))
            else:
                fpl[team][position] = [(player_id, player, cost)]
        else:
            fpl[team] = {position: [(player_id, player, cost)]}
clusters = []
print("team\tposition\tplayer\tplayer_id")
for team, team_values in fplgameweek.items():
    for position in team_values:
        candidates = fpl[team][position]
        seen = set()
        player_and_costs = list(team_values[position])
        loop_at = None
        while len(player_and_costs) > 0:
            player, cost = player_and_costs.pop(0)
            if (player, cost) == loop_at:
                ordered_candidates = sorted((abs(c - cost), (pid, p, c)) for pid, p, c in candidates)
                if ordered_candidates[0][0] == ordered_candidates[1][0]:
                    print("Error: no suitable candidate.")
                    exit(1)
                else:
                    loop_at = None
                    candidates = [c for c in candidates if c[0] != candidates[0][0]]
                    print(team, position, player, candidates[0][0], sep="\t")
            else:
                if loop_at is None:
                    loop_at = (player, cost)
                normalised_player = set(
                    sub("[^a-z ]", "", s)
                    for s in
                    normalize("NFD", sub("[-.]", " ", player)).split()
                    if len(s) > 2
                )
                best_candidate = None
                best_intersect = 0
                if len(candidates) > 1:
                    for candidate_id, candidate, c_cost in candidates:
                        normalised_candidate = set(
                            sub("[^a-z ]", "", s)
                            for s in normalize(
                                "NFD", sub("[-.]", " ", candidate)
                            ).split()
                            if len(s) > 2
                        )
                        overlap = normalised_player.intersection(normalised_candidate)
                        overlap_size = len(overlap)
                        if overlap_size > best_intersect:
                            best_intersect = overlap_size
                            best_candidate = (candidate_id, candidate, c_cost)
                else:
                    best_candidate = candidates[0]
                if best_candidate is None:
                    player_and_costs.append((player, cost))
                else:
                    loop_at = None
                    candidates = [c for c in candidates if c[0] != best_candidate[0]]
                    print(team, position, player, best_candidate[0], sep="\t")
