#!/usr/bin/python3
from itertools import combinations, product, chain
from math import log
from struct import pack
import sys
#from tqdm import tqdm

SQUAD_MAKEUP = [2, 5, 5, 3]
FORMATIONS = [
    [1, 3, 4, 3],
    [1, 3, 5, 2],
    [1, 4, 3, 3],
    [1, 4, 4, 2],
    [1, 5, 2, 3],
    [1, 5, 3, 2],
    [1, 5, 4, 1],
]
players = []
goalkeepers = set()
defenders = set()
midfielders = set()
forwards = set()
players_per_team = []
lowest_cost_per_position = {}
GKP = 0
DEFF = 1
MID = 2
FWD = 3
POSITION_INDEX = {
    "GKP": GKP,
    "DEF": DEFF,
    "MID": MID,
    "FWD": FWD,
}
player_id_index = {}
player_id_rev_index = {}
team_id_index = {}
team_id_rev_index = {}
player_positions_f = open("data/bin/player_positions.bin", "wb")
player_teams_f = open("data/bin/player_teams.bin", "wb")
player_costs_f = open("data/bin/player_costs.bin", "wb")
with open("data/parsed/players.csv") as players_f:
    indices = {}
    for i, line in enumerate(players_f):
        row = line.strip().strip().split(",")
        if i == 0:
            for j, col in enumerate(row): indices[col] = j
            continue
        external_player_id = int(row[indices["player_id"]])
        position = POSITION_INDEX[row[indices["position"]]]
        first_name = row[indices["first_name"]]
        second_name = row[indices["second_name"]]
        external_team_id = int(row[indices["team_id"]])
        if external_team_id in team_id_rev_index:
            team_id = team_id_rev_index[external_team_id]
        else:
            team_id = len(team_id_index)
            team_id_index[team_id] = external_team_id
            team_id_rev_index[external_team_id] = team_id
        cost = float(row[indices["cost"]])
        player_id = len(player_id_index)
        player_id_index[player_id] = external_player_id
        player_id_rev_index[external_player_id] = player_id
        while len(players) <= player_id: players.append(None)
        players[player_id] = (
            first_name,
            second_name,
            position,
            team_id,
            cost,
        )
        player_positions_f.write(pack("<B", position))
        player_teams_f.write(pack("<B", team_id))
        player_costs_f.write(pack("<f", cost))
        while len(players_per_team) <= team_id: players_per_team.append([])
        while len(players_per_team[team_id]) <= position:
            players_per_team[team_id].append(0)
        players_per_team[team_id][position] |= 1 << player_id
        if position == GKP: goalkeepers.add(player_id)
        elif position == DEFF: defenders.add(player_id)
        elif position == MID: midfielders.add(player_id)
        elif position == FWD: forwards.add(player_id)
        if position in lowest_cost_per_position:
            lowest_cost_per_position[position] = min([lowest_cost_per_position[position], cost])
        else:
            lowest_cost_per_position[position] = cost
player_positions_f.close()
player_teams_f.close()
player_costs_f.close()
players_per_team_f = open("data/bin/players_per_team.bin", "wb")
def bitset_iterator(bitset):
    i = 0
    while bitset != 0:
        if bitset & 1 == 1:
            yield i
        bitset >>= 1
        i += 1
for team in players_per_team:
    for position_players in team:
        some_players = list(bitset_iterator(position_players))
        players_per_team_f.write(pack("<B", len(some_players)))
        for player in some_players:
            players_per_team_f.write(pack("<H", player))
players_per_team_f.close()
squad_goalkeepers = set()
squad_defenders = set()
squad_midfielders = set()
squad_forwards = set()
with open("data/static/current_squad.csv") as current_squad_r:
    for i, line in enumerate(current_squad_r):
        external_player_id, paid_str = line.strip().split("\t")
        if i == 0: continue
        player_id = player_id_rev_index[int(external_player_id)]
        paid = int(paid_str)
        position = players[player_id][2]
        if position == GKP:
            squad_goalkeepers.add((player_id, paid))
        elif position == DEFF:
            squad_defenders.add((player_id, paid))
            defenders.remove(player_id)
        elif position == MID:
            squad_midfielders.add((player_id, paid))
            midfielders.remove(player_id)
        elif position == FWD:
            squad_forwards.add((player_id, paid))
            forwards.remove(player_id)
with open("data/static/current_balance") as balance_f:
    current_balance = float(balance_f.read())
squad_f = open("data/bin/current_squad.bin", "wb")
squad_f.write(pack("<f", current_balance))
for player, paid in chain(
    squad_goalkeepers, squad_defenders, squad_midfielders, squad_forwards
):
    squad_f.write(pack("<H", player))
    squad_f.write(pack("<H", paid))
squad_f.close()
player_season_prediction = {}
player_gameweek_predictions = []
with open("data/parsed/predictions.csv") as predictions_f:
    indices = {}
    for i, line in enumerate(predictions_f):
        row = line.strip().split(",")
        if i == 0:
            for j, col in enumerate(row): indices[col] = j
            continue
        player_id = player_id_rev_index[int(row[indices["player_id"]])]
        gameweek = int(row[indices["gameweek"]])
        predicted_pts = float(row[indices["predicted_pts"]])
        predicted_mins = float(row[indices["predicted_mins"]])
        if player_id in player_season_prediction:
            player_season_prediction[player_id][0] += predicted_mins
            player_season_prediction[player_id][1] += predicted_pts
            player_season_prediction[player_id][2] = (
                max([player_season_prediction[player_id][2], predicted_mins])
            )
            while len(player_gameweek_predictions) <= player_id:
                player_gameweek_predictions.append([])
            player_gameweek_predictions[player_id].append(predicted_pts)
        else:
            player_season_prediction[player_id] = (
                [predicted_mins, predicted_pts, predicted_mins]
            )
            while len(player_gameweek_predictions) <= player_id:
                player_gameweek_predictions.append([])
            player_gameweek_predictions[player_id].append(predicted_pts)
player_gameweek_predictions_f = open("data/bin/player_gameweek_predictions.bin", "wb")
games_remaining = max(len(x) for x in player_gameweek_predictions)
for player_games in player_gameweek_predictions:
    while len(player_games) < games_remaining:
        player_games.insert(0, 0)
    for score in player_games:
        player_gameweek_predictions_f.write(pack("<f", score))
player_gameweek_predictions_f.close()
limit = 80
def hits(lst):
    hit_dict = {}
    for item in lst:
        if item in hit_dict:
            hit_dict[item] += 1
        else:
            hit_dict[item] = 1
    return hit_dict
def to_bitset(iterable):
    bitset = 0
    for item in iterable: bitset |= 1 << item
    return bitset
def bitset_diff(a, b):
    return a & ~b
good_candidates = []
good_players_f = open("data/bin/good_players.bin", "wb")
good_players_f.write(pack("<B", games_remaining))
for game in range(1, games_remaining + 1):
    good_candidates_this_week = set()
    log_value = log(games_remaining - game + 1, 2)
    checkup_points = [
        int(round(2 ** ((i / round(1 if log_value == 0 else log_value)) * log_value)))
        for i in range(int(round(log_value) + 1))
    ]
    for point in checkup_points:
        best_over_period = []
        for player_id, games in enumerate(player_gameweek_predictions):
            best_over_period.append(
                (sum(g for g in games[game-1:game-1+point]), player_id)
            )
        best_over_period.sort(reverse=True)
        good_candidates_this_week.update(set(player[1] for player in best_over_period[:limit]))
    good_goalkeepers = {
        candidate
        for candidate in good_candidates_this_week
        if players[candidate][2] == GKP
    }
    good_players_f.write(pack("<H", len(good_goalkeepers)))
    for player in good_goalkeepers: good_players_f.write(pack("<H", player))
    good_defenders = {
        candidate
        for candidate in good_candidates_this_week
        if players[candidate][2] == DEFF
    }
    good_players_f.write(pack("<H", len(good_defenders)))
    for player in good_defenders: good_players_f.write(pack("<H", player))
    good_midfielders = {
        candidate
        for candidate in good_candidates_this_week
        if players[candidate][2] == MID
    }
    good_players_f.write(pack("<H", len(good_midfielders)))
    for player in good_midfielders: good_players_f.write(pack("<H", player))
    good_forwards = {
        candidate
        for candidate in good_candidates_this_week
        if players[candidate][2] == FWD
    }
    good_players_f.write(pack("<H", len(good_forwards)))
    for player in good_forwards: good_players_f.write(pack("<H", player))
    good_candidates_this_week = [
        to_bitset(good_goalkeepers),
        to_bitset(good_defenders),
        to_bitset(good_midfielders),
        to_bitset(good_forwards),
    ]
    good_candidates.append(good_candidates_this_week)
good_players_f.close()
benchwarmers = set()
lowest_cost_starting_goalkeeper_cost = 9e99
lowest_cost_starting_goalkeepers = set()
lowest_cost_starting_defender_cost = 9e99
lowest_cost_starting_defenders = set()
lowest_cost_starting_midfielder_cost = 9e99
lowest_cost_starting_midfielders = set()
lowest_cost_starting_forward_cost = 9e99
lowest_cost_starting_forwards = set()
reasonable_play_time_per_position = {GKP: 80, DEFF: 60, MID: 45, FWD: 45}
for player_id, (predicted_mins, predicted_pts, max_predicted_mins) in (
    player_season_prediction.items()
):
    position = players[player_id][2]
    if predicted_pts < 1 or max_predicted_mins < 40:
        benchwarmers.add(player_id)
    if (
        predicted_mins > 45 * 38
        and max_predicted_mins >= reasonable_play_time_per_position[position]
    ):
        if position == GKP:
            low_cost_starters = lowest_cost_starting_goalkeepers
            low_cost_starter_cost = lowest_cost_starting_goalkeeper_cost
        if position == DEFF:
            low_cost_starters = lowest_cost_starting_defenders
            low_cost_starter_cost = lowest_cost_starting_defender_cost
        if position == MID:
            low_cost_starters = lowest_cost_starting_midfielders
            low_cost_starter_cost = lowest_cost_starting_midfielder_cost
        if position == FWD:
            low_cost_starters = lowest_cost_starting_forwards
            low_cost_starter_cost = lowest_cost_starting_forward_cost
        if players[player_id][4] == low_cost_starter_cost:
            low_cost_starters.add(player_id)
        elif players[player_id][4] < low_cost_starter_cost:
            low_cost_starters.clear()
            low_cost_starters.add(player_id)
            low_cost_starter_cost = players[player_id][4]
        if position == GKP:
            lowest_cost_starting_goalkeeper_cost = low_cost_starter_cost
        if position == DEFF:
            lowest_cost_starting_defender_cost = low_cost_starter_cost
        if position == MID:
            lowest_cost_starting_midfielder_cost = low_cost_starter_cost
        if position == FWD:
            lowest_cost_starting_forward_cost = low_cost_starter_cost
forwards_by_cost = sorted([(players[player_id][4], player_id) for player_id in forwards])
cheapest_forwards = [forward for forward in forwards_by_cost if forward[0] == forwards_by_cost[0][0]]
cheapest_forwards = sorted([(player_season_prediction[forward[1]][1], forward[1]) for forward in cheapest_forwards], reverse=True)
defenders_by_cost = sorted([(players[player_id][4], player_id) for player_id in defenders])
cheapest_defenders = [defender for defender in defenders_by_cost if defender[0] == defenders_by_cost[0][0]]
cheapest_defenders = sorted([(player_season_prediction[defender[1]][1], defender[1]) for defender in cheapest_defenders], reverse=True)
midfielders_by_cost = sorted([(players[player_id][4], player_id) for player_id in midfielders])
cheapest_midfielders = [midfielder for midfielder in midfielders_by_cost if midfielder[0] == midfielders_by_cost[0][0]]
cheapest_midfielders = sorted([(player_season_prediction[midfielder[1]][1], midfielder[1]) for midfielder in cheapest_midfielders], reverse=True)
goalkeepers_by_cost = sorted([(players[player_id][4], player_id) for player_id in goalkeepers])
cheapest_goalkeepers = [goalkeeper for goalkeeper in goalkeepers_by_cost if goalkeeper[0] == goalkeepers_by_cost[0][0]]
cheapest_goalkeepers = sorted([(player_season_prediction[goalkeeper[1]][1], goalkeeper[1]) for goalkeeper in cheapest_goalkeepers], reverse=True)
bargain_goalkeepers = set(player[1] for player in cheapest_goalkeepers[:1]).union(lowest_cost_starting_goalkeepers).difference(benchwarmers)
bargain_defenders = set(player[1] for player in cheapest_defenders[:2]).union(lowest_cost_starting_defenders).difference(benchwarmers)
bargain_midfielders = set(player[1] for player in cheapest_midfielders[:3]).union(lowest_cost_starting_midfielders).difference(benchwarmers)
bargain_forwards = set(player[1] for player in cheapest_forwards[:2]).union(lowest_cost_starting_forwards).difference(benchwarmers)
bargain_goalkeepers -= squad_goalkeepers
bargain_defenders -= squad_defenders
bargain_midfielders -= squad_midfielders
bargain_forwards -= squad_forwards
bargain_players_f = open("data/bin/bargain_players.bin", "wb")
bargain_players_f.write(pack("<H", len(bargain_goalkeepers)))
for player in bargain_goalkeepers:
    bargain_players_f.write(pack("<H", player))
bargain_players_f.write(pack("<H", len(bargain_defenders)))
for player in bargain_defenders:
    bargain_players_f.write(pack("<H", player))
bargain_players_f.write(pack("<H", len(bargain_midfielders)))
for player in bargain_midfielders:
    bargain_players_f.write(pack("<H", player))
bargain_players_f.write(pack("<H", len(bargain_forwards)))
for player in bargain_forwards:
    bargain_players_f.write(pack("<H", player))
bargain_players_f.close()
bargain_goalkeepers = to_bitset(bargain_goalkeepers)
bargain_defenders = to_bitset(bargain_defenders)
bargain_midfielders = to_bitset(bargain_midfielders)
bargain_forwards = to_bitset(bargain_forwards)
squad_goalkeepers_bs = to_bitset([p for p, _ in squad_goalkeepers])
squad_defenders_bs = to_bitset([p for p, _ in squad_defenders])
squad_midfielders_bs = to_bitset([p for p, _ in squad_midfielders])
squad_forwards_bs = to_bitset([p for p, _ in squad_forwards])
team_counts = [0] * len(team_id_index)
overrepresented_teams = [False] * len(team_id_index)
overrepresented_team_list = []
for player_id, _ in chain(
    squad_goalkeepers, squad_defenders, squad_midfielders, squad_forwards
):
    team_id = players[player_id][3]
    team_counts[team_id] = team_counts[team_id] + 1
    if team_counts[team_id] == 3:
        overrepresented_teams[team_id] = True
        overrepresented_team_list.append(team_id)

########################################################### SETUP ENDS HERE.

possible_transfers = []
def get_possible_transfers(offset):
    global current_balance;
    for player_id, _ in chain(
        squad_goalkeepers, squad_defenders, squad_midfielders, squad_forwards
    ):
        _, _, position, team_id, cost = players[player_id]
        if position == GKP:
            already_have = squad_goalkeepers_bs
            bargain_candidates = bargain_goalkeepers
        elif position == DEFF:
            already_have = squad_defenders_bs
            bargain_candidates = bargain_defenders
        elif position == MID:
            already_have = squad_midfielders_bs
            bargain_candidates = bargain_midfielders
        elif position == FWD:
            already_have = squad_forwards_bs
            bargain_candidates = bargain_forwards
        candidates = (
            bitset_diff(good_candidates[offset - 1][position], already_have)
            | bargain_candidates
        )
        if overrepresented_teams[team_id]:
            for t in overrepresented_team_list:
                if t != team_id:
                    candidates = bitset_diff(
                        candidates, players_per_team[t][position]
                    )
        else:
            for t in overrepresented_team_list:
                candidates = bitset_diff(
                    candidates, players_per_team[t][position]
                )
        for p in bitset_iterator(candidates):
            if round(players[p][4] * 10) <= round((cost + current_balance) * 10):
                possible_transfers.append((player_id, p))
    possible_transfers.append((None, None))
def apply_transfer(position, some_players, transfer_out, transfer_in):
    if transfer_out is not None:
        if transfer_out in some_players:
            some_players.remove(transfer_out)
            some_players.add(transfer_in)
def apply_bitset_transfer(position, some_players, transfer_out, transfer_in):
    if transfer_out is not None:
        if players[transfer_out][2] == position:
            if some_players & (1 << transfer_out) > 0:
                some_players &= ~(1 << transfer_out)
                some_players |= 1 << transfer_in
    return some_players
def next_balance(balance, transfer_out, transfer_in):
    if transfer_out is None: return balance
    credit = players[transfer_out][4]
    debit = players[transfer_in][4]
    return balance + credit - debit
best_score = 0
running_score = 0
best_transfer_seq= []
transfer_seq = []
def get_best_formation(offset):
    best_formation_score = 0
    best_formation = None
    best_captain = None
    for gkp, defence, mid, fwd in FORMATIONS:
        for formation in product(
            combinations([p for p, _ in squad_goalkeepers], gkp),
            combinations([p for p, _ in squad_defenders], defence),
            combinations([p for p, _ in squad_midfielders], mid),
            combinations([p for p, _ in squad_forwards], fwd),
        ):
            predicted_pts = 0
            captain = 0
            captain_id = None
            for pos in formation:
                for p in pos:
                    pts = player_gameweek_predictions[p][offset - 1]
                    predicted_pts += pts
                    if pts > captain:
                        captain = pts
                        captain_id = p
            predicted_pts += captain
            if predicted_pts > best_formation_score:
                best_formation_score = predicted_pts
                best_formation = formation
                best_captain = captain_id
    return best_formation_score, best_formation, best_captain
def best_transfer_sequence(max_depth, depth=1):
    global current_balance
    global best_score
    global running_score
    global best_transfer_seq
    global squad_goalkeepers
    global squad_defenders
    global squad_midfielders
    global squad_forwards
    global squad_goalkeepers_bs
    global squad_defenders_bs
    global squad_midfielders_bs
    global squad_forwards_bs
    global bargain_goalkeepers
    global bargain_defenders
    global bargain_midfielders
    global bargain_forwards
    pop_to = len(possible_transfers)
    get_possible_transfers(depth)
    while len(possible_transfers) > pop_to:
        transfer_out, transfer_in = possible_transfers.pop()
        #if depth == 1:
        #    print(str(len(possible_transfers)))
        transfer_seq.append((transfer_out, transfer_in))
        current_balance = (
            next_balance(current_balance, transfer_out, transfer_in)
        )
        if transfer_out is not None:
            out_team = players[transfer_out][3]
            in_team = players[transfer_in][3]
            if out_team != in_team:
                team_counts[out_team] -= 1
                team_counts[in_team] = team_counts[in_team] + 1
                if team_counts[out_team] == 2:
                    overrepresented_teams[out_team] = False
                    overrepresented_team_list.remove(out_team)
                if team_counts[in_team] == 3:
                    overrepresented_teams[in_team] = True
                    overrepresented_team_list.append(in_team)
        apply_transfer(GKP, squad_goalkeepers, transfer_out, transfer_in)
        apply_transfer(DEFF, squad_defenders, transfer_out, transfer_in)
        apply_transfer(MID, squad_midfielders, transfer_out, transfer_in)
        apply_transfer(FWD, squad_forwards, transfer_out, transfer_in)
        squad_goalkeepers_bs = (
            apply_bitset_transfer(
                GKP, squad_goalkeepers_bs, transfer_out, transfer_in
            )
        )
        squad_defenders_bs = (
            apply_bitset_transfer(
                DEFF, squad_defenders_bs, transfer_out, transfer_in
            )
        )
        squad_midfielders_bs = (
            apply_bitset_transfer(
                MID, squad_midfielders_bs, transfer_out, transfer_in
            )
        )
        squad_forwards_bs = (
            apply_bitset_transfer(
                FWD, squad_forwards_bs, transfer_out, transfer_in
            )
        )
        bargain_goalkeepers = (
            apply_bitset_transfer(
                GKP, bargain_goalkeepers, transfer_in, transfer_out
            )
        )
        bargain_defenders = (
            apply_bitset_transfer(
                DEFF, bargain_defenders, transfer_in, transfer_out
            )
        )
        bargain_midfielders = (
            apply_bitset_transfer(
                MID, bargain_midfielders, transfer_in, transfer_out
            )
        )
        bargain_forwards = (
            apply_bitset_transfer(
                FWD, bargain_forwards, transfer_in, transfer_out
            )
        )
        best_formation_score, formation, captain = get_best_formation(depth)
        running_score += best_formation_score
        if depth < max_depth:
            best_transfer_sequence(max_depth, depth + 1)
        else:
            if running_score > best_score:
                best_score = running_score
                best_transfer_seq = transfer_seq[:]
                print("good score:", best_score, best_transfer_seq)
        running_score -= best_formation_score
        bargain_forwards = (
            apply_bitset_transfer(
                FWD, bargain_forwards, transfer_out, transfer_in
            )
        )
        bargain_midfielders = (
            apply_bitset_transfer(
                MID, bargain_midfielders, transfer_out, transfer_in
            )
        )
        bargain_defenders = (
            apply_bitset_transfer(
                DEFF, bargain_defenders, transfer_out, transfer_in
            )
        )
        bargain_goalkeepers = (
            apply_bitset_transfer(
                GKP, bargain_goalkeepers, transfer_out, transfer_in
            )
        )
        squad_forwards_bs = (
            apply_bitset_transfer(
                FWD, squad_forwards_bs, transfer_in, transfer_out
            )
        )
        squad_midfielders_bs = (
            apply_bitset_transfer(
                MID, squad_midfielders_bs, transfer_in, transfer_out
            )
        )
        squad_defenders_bs = (
            apply_bitset_transfer(
                DEFF, squad_defenders_bs, transfer_in, transfer_out
            )
        )
        squad_goalkeepers_bs = (
            apply_bitset_transfer(
                GKP, squad_goalkeepers_bs, transfer_in, transfer_out
            )
        )
        apply_transfer(FWD, squad_forwards, transfer_in, transfer_out)
        apply_transfer(MID, squad_midfielders, transfer_in, transfer_out)
        apply_transfer(DEFF, squad_defenders, transfer_in, transfer_out)
        apply_transfer(GKP, squad_goalkeepers, transfer_in, transfer_out)
        if transfer_out is not None:
            if out_team != in_team:
                team_counts[in_team] -= 1
                team_counts[out_team] += 1
                if team_counts[in_team] == 2:
                    overrepresented_teams[in_team] = False
                    overrepresented_team_list.remove(in_team)
                if team_counts[out_team] == 3:
                    overrepresented_teams[out_team] = True
                    overrepresented_team_list.append(out_team)
        current_balance = (
            next_balance(current_balance, transfer_in, transfer_out)
        )
        transfer_seq.pop()
best_transfer_sequence(1)
print(best_score, "is the best predicted score.")
best_formation_score, formation, captain = get_best_formation(1)
for row in formation:
    print("\t".join([players[i][0] + " " + players[i][1] for i in row]))
print("Captain:" + players[captain][0] + " " + players[captain][1])
print(best_transfer_seq)
sys.stdout.write("=============================================\n")
for i, (transfer_out, transfer_in) in enumerate(best_transfer_seq, start=1):
    if transfer_out is None:
        print("NO TRANSFER.")
    else:
        apply_transfer(GKP, squad_goalkeepers, transfer_out, transfer_in)
        apply_transfer(DEFF, squad_defenders, transfer_out, transfer_in)
        apply_transfer(MID, squad_midfielders, transfer_out, transfer_in)
        apply_transfer(FWD, squad_forwards, transfer_out, transfer_in)
        best_formation_score, best_formation, best_captain = get_best_formation(i)
        print("\t" +
            players[transfer_out][0] + " " + players[transfer_out][1] +
            " ==> " +
            players[transfer_in][0] + " " + players[transfer_in][1]
        )
        print(best_formation_score)
for the_id in player_id_index.keys():
    print(the_id, player_id_index[int(the_id)])
print(team_id_index)
