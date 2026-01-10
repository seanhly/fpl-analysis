#!/usr/bin/python
from unicodedata import normalize
import csv
from re import sub, match

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

managerbotten = {}
with open("sources/managerbotten.dk.players.tsv", mode="r") as file:
    r = csv.reader(file, delimiter="\t")
    for team, position, player, player_short_name, cost, owned_by in r:
        cost = int(float(cost) * 10 + 0.1)
        if team in managerbotten:
            if position in managerbotten[team]:
                managerbotten[team][position].append((player, player_short_name, cost, team))
            else:
                managerbotten[team][position] = [(player, player_short_name, cost, team)]
        else:
            managerbotten[team] = {position: [(player, player_short_name, cost, team)]}
    to_map = list(managerbotten.keys())
    while len(to_map) > 0:
        to_map_team = to_map.pop(0)
        if to_map_team in valid_teams:
            valid_teams.remove(to_map_team)
        elif len(valid_teams) == 1:
            managerbotten[list(valid_teams)[0]] = managerbotten[to_map_team]
            del managerbotten[to_map_team]
            valid_teams.clear()
        else:
            parts = set(part for part in to_map_team.split() if len(part) > 2)
            best = None
            best_intersect = 0
            for team in valid_teams:
                valid_parts = set(part for part in team.split() if len(part) > 2)
                intersect = parts.intersection(valid_parts)
                if len(intersect) > best_intersect:
                    best_intersect = len(intersect)
                    best = team
                elif len(intersect) == best_intersect:
                    best = None
            if best is None:
                matches = [
                    team
                    for team in valid_teams
                    if match(team.replace("", ".*")[2:-2] + "$", to_map_team) is not None
                ]
                if len(matches) == 1:
                    managerbotten[matches[0]] = managerbotten[to_map_team]
                    del managerbotten[to_map_team]
                    valid_teams.remove(matches[0])
                else:
                    to_map.append(to_map_team)
            else:
                managerbotten[best] = managerbotten[to_map_team]
                del managerbotten[to_map_team]
                valid_teams.remove(best)

clusters = []
print("team\tposition\tplayer\tplayer_id")
for sanitised_team, team_values in managerbotten.items():
    for position in team_values:
        candidates = fpl[sanitised_team][position]
        seen = set()
        player_and_costs = list(team_values[position])
        loop_at = None
        while len(player_and_costs) > 0:
            player, player_short_name, cost, team = player_and_costs.pop(0)
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
                        alternative_player, alternative_cost = player_and_costs[0]
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
                            print(team, position, player, alternative_remainder[0][0], sep="\t")
                            candidates = [c for c in candidates if c[0] != alternative_remainder[0][0]]
                        else:
                            print("Error: no suitable candidate.")
                            exit(1)
                else:
                    loop_at = None
                    print(team, position, player, candidates[0][0], sep="\t")
                    candidates = [c for c in candidates if c[0] != candidates[0][0]]
            else:
                if loop_at is None:
                    loop_at = (player, cost)
                normalised_player = set(
                    sub("[^a-z ]", "", s)
                    for s in
                    normalize("NFD", sub("[-.]", " ", player + " " + player_short_name)).split()
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
                            best_candidate = (candidate_id, candidate, c_cost, team)
                else:
                    best_candidate = candidates[0]
                if best_candidate is None:
                    player_and_costs.append((player, player_short_name, cost, team))
                else:
                    loop_at = None
                    print(team, position, player, best_candidate[0], sep="\t")
                    candidates = [c for c in candidates if c[0] != best_candidate[0]]
