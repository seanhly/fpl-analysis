#!/usr/bin/python
from unicodedata import normalize
import csv
from re import sub

valid_teams = set()
fpl = {}
with open("sources/fpl.players.tsv", mode="r") as file:
    r = csv.reader(file, delimiter="\t")
    for player_id, team, position, player, cost in r:
        valid_teams.add(team)
        player_id = int(player_id)
        cost = int(float(cost) * 10 + 0.1)
        if team in fpl:
            if position in fpl[team]:
                fpl[team][position].append((player_id, player, cost))
            else:
                fpl[team][position] = [(player_id, player, cost)]
        else:
            fpl[team] = {position: [(player_id, player, cost)]}

fantasyfootballpundit = {}
with open("sources/fantasyfootballpundit.com.players.tsv", mode="r") as file:
    r = csv.reader(file, delimiter="\t")
    for team, position, player, cost, owned_by in r:
        cost = int(float(cost) * 10 + 0.1)
        if team in fantasyfootballpundit:
            if position in fantasyfootballpundit[team]:
                fantasyfootballpundit[team][position].append((player, cost, team))
            else:
                fantasyfootballpundit[team][position] = [(player, cost, team)]
        else:
            fantasyfootballpundit[team] = {position: [(player, cost, team)]}
    to_map = list(fantasyfootballpundit.keys())
    while len(to_map) > 0:
        to_map_team = to_map.pop(0)
        if to_map_team in valid_teams:
            valid_teams.remove(to_map_team)
        elif len(valid_teams) == 1:
            fantasyfootballpundit[list(valid_teams)[0]] = fantasyfootballpundit[to_map_team]
            del fantasyfootballpundit[to_map_team]
        else:
            to_map.append(to_map_team)

clusters = []
print("team\tposition\tplayer\tplayer_id")
for sanitised_team, team_values in fantasyfootballpundit.items():
    for position in team_values:
        candidates = fpl[sanitised_team][position]
        seen = set()
        player_and_costs = list(team_values[position])
        loop_at = None
        while len(player_and_costs) > 0:
            player, cost, team = player_and_costs.pop(0)
            if (player, cost) == loop_at:
                ordered_candidates = sorted(
                    (
                        abs(c - cost),
                        (pid, p, c),
                    )
                    for pid, p, c in candidates
                )
                if ordered_candidates[0][0] == ordered_candidates[1][0]:
                    if len(player_and_costs) == 1:
                        alternative_player, alternative_cost, team = player_and_costs[0]
                        alternative_candidates = sorted(
                            (abs(c - alternative_cost), (pid, p, c))
                            for pid, p, c in candidates
                        )
                        alternative_remainder = [
                            (pid, p, c)
                            for s, (pid, p, c) in alternative_candidates
                            if s != alternative_candidates[0][0]
                        ]
                        if len(alternative_remainder) == 1:
                            loop_at = None
                            candidates = [c for c in candidates if c[0] != alternative_remainder[0][0]]
                            print(team, position, player, alternative_remainder[0][0], sep="\t")
                        else:
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
                                "NFD", sub("[-.]", " ", sub("[ı]", "i", candidate))
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
                    player_and_costs.append((player, cost, team))
                else:
                    loop_at = None
                    candidates = [c for c in candidates if c[0] != best_candidate[0]]
                    print(team, position, player, best_candidate[0], sep="\t")
