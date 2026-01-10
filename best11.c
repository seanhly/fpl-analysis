#include <stdio.h>
#include <signal.h>
#include <math.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <stdbool.h>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cstdarg>
#include <unistd.h>
#include <cstring>
#include <openssl/evp.h>

#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))

#define WILDCARD_LOOKAHEAD 1
#define SQUAD_SIZE 15
#define WEEKS_IN_SEASON 38
#define NULL_IDX 0xF
#define CHIPS 4
#define TEAMS 20
#define POSITIONS 4

#define USED_BENCHBOOST true
#define USED_FREEHIT true
#define USED_WILDCARD false
#define WILDCARD_TRANSFERS 15
#define USED_TRIPLE true

#define DOUBLE_TRANSFER true

using namespace std;

FILE *ideal_wildcards;
void exit_handler(int _) {
	if (ideal_wildcards != NULL) {
		fclose(ideal_wildcards);
		unlink("data/bin/ideal_wildcards.bin");
	}
	exit(0);
}

typedef unsigned long long ui64;
typedef unsigned int ui32;
typedef unsigned short ui16;
typedef unsigned char ui8;

typedef struct { ui64 bits[2]; } Bitset;

ui8 outHash[32];
ui64 hash_bitset(const Bitset *data) {
	EVP_MD_CTX* ctx = EVP_MD_CTX_new();
	if (!ctx) {
		fprintf(stderr, "Failed to create EVP_MD_CTX\n");
		exit(1);
	}
	if (1 != EVP_DigestInit_ex(ctx, EVP_sha256(), nullptr)) {
		fprintf(stderr, "DigestInit failed\n");
		EVP_MD_CTX_free(ctx);
		exit(1);
	}
	int size = POSITIONS * sizeof(Bitset);
	if (1 != EVP_DigestUpdate(ctx, data, (size_t) size)) {
		fprintf(stderr, "DigestUpdate failed\n");
		EVP_MD_CTX_free(ctx);
		exit(1);
	}
	if (1 != EVP_DigestFinal_ex(ctx, outHash, NULL)) {
		fprintf(stderr, "DigestFinal failed\n");
		EVP_MD_CTX_free(ctx);
		exit(1);
	}

	EVP_MD_CTX_free(ctx);
	ui64 h = 0;
	for (ui64 i = 0; i < 8; ++i)
		h |= ((ui64) outHash[i]) << (8L * i);
	return h;
}

typedef struct {
	ui8 surplus_defenders: 2;
	ui8 surplus_midfielders: 2;
} Formation;

typedef struct {
	float score;
	Formation formation;
} BestFormation;

typedef ui16 pid;
typedef ui8 tid;

pid NO_TRANSFER  = 0b1111111;
pid FREE_HIT     = 0b1111110;
pid WILDCARD     = 0b1111101;

unsigned int ARSENAL = -1;
unsigned int ASTON_VILLA = -1;
unsigned int MANU = -1;
unsigned int MAN_CITY = -1;
unsigned int BRENTFORD = -1;

typedef enum {
	GKP,
	DEF,
	MID,
	FWD,
} Position;

char *POSITION_LABELS[POSITIONS] =
	{ (char*) "GKP", (char*) "DEF", (char*) "MID", (char*) "FWD" };

typedef enum {
	GKP1, GKP2, DEF1, DEF2, DEF3, DEF4, DEF5,
	MID1, MID2, MID3, MID4, MID5, FWD1, FWD2, FWD3,
} SquadMember;

SquadMember POSITION_OFFSETS[POSITIONS][2] =
	{{GKP1, GKP2}, {DEF1, DEF5}, {MID1, MID5}, {FWD1, FWD3}};

ui8 SWING_SQUAD_POSITIONS[7] = {DEF4, DEF5, MID3, MID4, MID5, FWD2, FWD3};
ui8 DEFAULT_SQUAD_POSITIONS[7] = {GKP1, DEF1, DEF2, DEF3, MID1, MID2, FWD1};

SquadMember SQUAD[SQUAD_SIZE] = {
	         GKP1, GKP2,
	DEF1, DEF2, DEF3, DEF4, DEF5,
	MID1, MID2, MID3, MID4, MID5,
	      FWD1, FWD2, FWD3
};

ui8 SQUAD_MAKEUP[POSITIONS] = {2, 5, 5, 3};

float best_score = 0;
float running_score = 0;

void set_bit(Bitset *bitset, ui16 bit) {
	ui64 big_offset = bit / 64L;
	ui64 little_offset = bit % 64L;
	bitset->bits[big_offset] |= 1L << little_offset;
}
void clear_bit(Bitset *bitset, ui16 bit) {
	ui64 big_offset = bit / 64L;
	ui64 little_offset = bit % 64L;
	bitset->bits[big_offset] &= ~(1L << little_offset);
}
bool is_bit_set(Bitset *bitset, ui16 bit) {
	ui64 big_offset = bit / 64L;
	ui64 little_offset = bit % 64L;
	return (bitset->bits[big_offset] & (1L << little_offset)) > 0;
}
void print_bitset(Bitset bitset) {
	for (int i = 0; i < 2; ++i) {
		for (ui64 j = 0; j < 64; ++j) {
			if (bitset.bits[i] & (1L << j)) printf("1");
			else printf("0");
		}
		printf(" ");
	}
	printf("\n"); fflush(stdout);
}
void bitset_diff(Bitset *a, Bitset *b, Bitset *c) {
	for (int i = 0; i < 2; ++i)
		c->bits[i] = a->bits[i] & ~b->bits[i];
}
void bitset_union(Bitset *a, Bitset *b, Bitset *c) {
	for (int i = 0; i < 2; ++i) {
		c->bits[i] = a->bits[i] | b->bits[i];
	}
}
Bitset new_bitset() {
	Bitset bitset;
	for (int i = 0; i < 2; ++i) bitset.bits[i] = 0;
	return bitset;
}

typedef struct {
	ui8 out_idx: 4;
	pid transfer_out: 7;
	pid transfer_in: 7;
	bool triple_captain: 1;
	bool bench_boost: 1;
	bool double_sub: 1;
} Transfer;

typedef struct {
	char *first_name;
	char *last_name;
	Position position;
	tid team_id;
	ui16 cost;
	ui16 taxed_cost;
	ui16 id;
} Player;

typedef struct {
	Position position: 2;
	pid i: 14;
} PlayerID;
bool operator==(const PlayerID& a, const PlayerID& b) {
	return a.position == b.position && a.i == b.i;
}

ui8 CONSTANTS_L = 0;
PlayerID CONSTANTS[15];
bool USE_CONSTANTS = true;

Player players[POSITIONS][128];
ui16 players_l[POSITIONS];
PlayerID players_by_score[WEEKS_IN_SEASON][2000];
ui16 players_by_score_l;

Transfer best_transfer_seq[WEEKS_IN_SEASON];
ui8 best_transfer_seq_l;
float best_scores[WEEKS_IN_SEASON];
float the_best_scores[WEEKS_IN_SEASON];
Transfer transfer_seq[WEEKS_IN_SEASON];
ui32 transfer_seq_l = 0;

Position index_to_position(ui32 idx) {
	for (ui8 p = GKP; p <= MID; ++p) if (idx <= POSITION_OFFSETS[p][1]) return (Position) p;
	return FWD;
}

pid current_squad[SQUAD_SIZE];

float read_float(FILE *f) {
	float v;
	int unused = fread((void*)(&v), sizeof(v), 1, f);
	return v;
}

ui16 read_short(FILE *f) {
	ui16 v;
	int unused = fread((void*)(&v), sizeof(v), 1, f);
	return v;
}

ui8 read_char(FILE *f) {
	ui8 v;
	int unused = fread((void*)(&v), sizeof(v), 1, f);
	return v;
}

pid dream_squad[SQUAD_SIZE];
pid best_dream_squad[SQUAD_SIZE];
Bitset current_squad_bs[POSITIONS];
int overrepresented_team_c;
tid overrepresented_team_list[SQUAD_SIZE / 3];
bool overrepresented_teams[TEAMS] = {false};
int team_counts[TEAMS] = {0};
Bitset candidates;
Bitset bargain_players[POSITIONS];
Bitset *good_candidates[POSITIONS];
Bitset players_per_team[TEAMS][POSITIONS];
ui16 balance;
ui16 team_value = 0;

pid starting_squad[SQUAD_SIZE];
ui16 starting_balance;
Bitset starting_squad_bs[POSITIONS];
int starting_overrepresented_team_c;
tid starting_overrepresented_team_list[SQUAD_SIZE / 3];
bool starting_overrepresented_teams[TEAMS] = {false};
int starting_team_counts[TEAMS] = {0};

void remove_from_list(tid *list, int *length_ptr, tid item) {
	int length = *length_ptr;
	int i = length - 1;
	for (; i >= 0; --i)
		if (list[i] == item) break;
	list[i] = list[length - 1];
	*length_ptr = length - 1;
}

float player_gameweek_predictions[POSITIONS][128][WEEKS_IN_SEASON];
int games_remaining;

void print_squad(pid *s, int gw) {
	for (int j = GKP; j <= FWD; ++j) {
		printf("\t");
		for (int i = POSITION_OFFSETS[j][0]; i <= POSITION_OFFSETS[j][1]; ++i) {
			if (s[i] == NO_TRANSFER) printf(
				"%c%d:%u[NA] ",
				POSITION_LABELS[j][0],
				i - POSITION_OFFSETS[j][0] + 1,
				players[j][s[i]].id
			);
			else printf(
				"%c%d:%u[%0.1f] ",
				POSITION_LABELS[j][0],
				i - POSITION_OFFSETS[j][0] + 1,
				players[j][s[i]].id,
				player_gameweek_predictions[j][s[i]][gw - 1]
			);
		}
		printf("\n");
	}
	fflush(stdout);
}

Position context_pos;
ui8 gameweek_lo;
ui8 gameweek_hi;
int compare(const void *a1, const void *a2) {
  	pid p1 = *(pid*) a1;
	pid p2 = *(pid*) a2;
	float pts1 = 0;
	float pts2 = 0;
	for (ui8 gameweek = gameweek_lo; gameweek <= gameweek_hi; ++gameweek) {
		pts1 += player_gameweek_predictions[context_pos][p1][gameweek - 1];
		pts2 += player_gameweek_predictions[context_pos][p2][gameweek - 1];
	}
	if (pts1 > pts2) return -1;
	if (pts1 < pts2) return +1;
	return 0;
}

int compare_player_id(const void *a1, const void *a2) {
  	PlayerID p1 = *(PlayerID*) a1;
	PlayerID p2 = *(PlayerID*) a2;
	float pts1 = 0;
	float pts2 = 0;
	for (ui8 gameweek = gameweek_lo; gameweek <= gameweek_hi; ++gameweek) {
		pts1 += player_gameweek_predictions[p1.position][p1.i][gameweek - 1];
		pts2 += player_gameweek_predictions[p2.position][p2.i][gameweek - 1];
	}
	if (pts1 > pts2) return -1;
	if (pts1 < pts2) return +1;
	return 0;
}

pid context_squad[SQUAD_SIZE];
int compare_in_squad(const void *a1, const void *a2) {
  	ui8 i1 = *(pid*) a1;
	ui8 i2 = *(pid*) a2;
	pid p1 = context_squad[i1];
	pid p2 = context_squad[i2];
	Position p1_pos = index_to_position(i1);
	Position p2_pos = index_to_position(i2);
	float pts1 = 0;
	float pts2 = 0;
	for (ui8 gameweek = gameweek_lo; gameweek <= gameweek_hi; ++gameweek) {
		pts1 += player_gameweek_predictions[p1_pos][p1][gameweek - 1];
		pts2 += player_gameweek_predictions[p2_pos][p2][gameweek - 1];
	}
	if (pts1 > pts2) return -1;
	if (pts1 < pts2) return +1;
	return 0;
}

void sort_squad(pid *squad, ui8 gameweek) {
	gameweek_lo = gameweek;
	gameweek_hi = gameweek;
	for (ui8 p = GKP; p <= FWD; ++p) {
		context_pos = (Position) p;
		qsort(&squad[POSITION_OFFSETS[p][0]], SQUAD_MAKEUP[p], sizeof(pid), compare);
	}
}

pid default_pts_per_position[POSITIONS][5];
BestFormation get_best_formation_score(
	ui8 gameweek, pid *squad, bool triple_captain, ui8 transfers
) {
	ui8 offsets[POSITIONS] = {0, 0, 0, 0};
	for (int i = 0; i < SQUAD_SIZE; ++i)
		if (squad[i] == NO_TRANSFER) {
			Position p = index_to_position(i);
			context_squad[i] = default_pts_per_position[p][offsets[p]++];
		} else context_squad[i] = squad[i];
	sort_squad(context_squad, gameweek);
	ui8 surplus_defenders = 0;
	ui8 surplus_midfielders = 0;
	for (ui8 t = 0; t < transfers; ++t) {
		pid max_in;
		float max_diff = 0;
		ui8 max_i;
		for (ui8 i = 0; i < SQUAD_SIZE; ++i) {
			Position p = index_to_position(i);
			pid in = default_pts_per_position[p][0];
			float default_pts;
			if (in == NO_TRANSFER) default_pts = 0;
			else default_pts = player_gameweek_predictions[p][in][gameweek - 1];
			pid out = context_squad[i];
			float actual_pts = player_gameweek_predictions[p][out][gameweek - 1];
			if (actual_pts > default_pts) continue;
			float diff = default_pts - actual_pts;
			if (diff > max_diff) {
				max_diff = diff;
				max_in = in;
				max_i = i;
			}
		}
		if (max_diff == 0) break;
		context_squad[max_i] = max_in;
	}
	float score = 0;
	float captain = 0;
	for (int i = 0; i < 7; ++i) {
		ui8 idx = DEFAULT_SQUAD_POSITIONS[i];
		Position position = index_to_position(idx);
		pid p = context_squad[idx];
		float pts;
		if (p == NO_TRANSFER) pts = 0;
		else pts = player_gameweek_predictions[position][p][gameweek - 1];
		score += pts;
		if (pts > captain) captain = pts;
	}
	qsort(&SWING_SQUAD_POSITIONS, 7, sizeof(ui8), compare_in_squad);
	for (int i = 0; i < 4; ++i) {
		ui8 j = SWING_SQUAD_POSITIONS[i];
		Position position = index_to_position(j);
		pid p = context_squad[j];
		float pts;
		if (p == NO_TRANSFER) pts = 0;
		else {
			pts = player_gameweek_predictions[position][p][gameweek - 1];
			switch (position) {
				case DEF: ++surplus_defenders; break;
				case MID: ++surplus_midfielders; break;
			}
		}
		score += pts;
	}
	return {
		score + captain * (1 + triple_captain),
		{surplus_defenders, surplus_midfielders}
	};
}

typedef struct {
	float scores[4];
} PositionScores;

PositionScores get_best_formation_cutoffs_per_position(
	ui8 gameweek, pid *squad, bool triple_captain, ui8 transfers
) {
	ui8 offsets[POSITIONS] = {0, 0, 0, 0};
	for (int i = 0; i < SQUAD_SIZE; ++i)
		if (squad[i] == NO_TRANSFER) {
			Position p = index_to_position(i);
			context_squad[i] = default_pts_per_position[p][offsets[p]++];
		} else context_squad[i] = squad[i];
	sort_squad(context_squad, gameweek);
	ui8 surplus_defenders = 0;
	ui8 surplus_midfielders = 0;
	for (ui8 t = 0; t < transfers; ++t) {
		pid max_in;
		float max_diff = 0;
		ui8 max_i;
		for (ui8 i = 0; i < SQUAD_SIZE; ++i) {
			Position p = index_to_position(i);
			pid in = default_pts_per_position[p][0];
			float default_pts;
			if (in == NO_TRANSFER) default_pts = 0;
			else default_pts = player_gameweek_predictions[p][in][gameweek - 1];
			pid out = context_squad[i];
			float actual_pts = player_gameweek_predictions[p][out][gameweek - 1];
			if (actual_pts > default_pts) continue;
			float diff = default_pts - actual_pts;
			if (diff > max_diff) {
				max_diff = diff;
				max_in = in;
				max_i = i;
			}
		}
		if (max_diff == 0) break;
		context_squad[max_i] = max_in;
	}
	float min_score = 1e10;
	PositionScores min_score_per_position;
	min_score_per_position.scores[GKP] = 1e10;
	min_score_per_position.scores[DEF] = 1e10;
	min_score_per_position.scores[MID] = 1e10;
	min_score_per_position.scores[FWD] = 1e10;
	for (int i = 0; i < 7; ++i) {
		ui8 idx = DEFAULT_SQUAD_POSITIONS[i];
		Position position = index_to_position(idx);
		pid p = context_squad[idx];
		float pts;
		if (p == NO_TRANSFER) pts = 0;
		else pts = player_gameweek_predictions[position][p][gameweek - 1];
		if (position != GKP && pts < min_score) min_score = pts;
		if (pts < min_score_per_position.scores[position])
			min_score_per_position.scores[position] = pts;
	}
	qsort(&SWING_SQUAD_POSITIONS, 7, sizeof(ui8), compare_in_squad);
	for (int i = 0; i < 4; ++i) {
		ui8 j = SWING_SQUAD_POSITIONS[i];
		Position position = index_to_position(j);
		pid p = context_squad[j];
		float pts;
		if (p == NO_TRANSFER) pts = 0;
		else {
			pts = player_gameweek_predictions[position][p][gameweek - 1];
			switch (position) {
				case DEF: ++surplus_defenders; break;
				case MID: ++surplus_midfielders; break;
			}
		}
		if (position != GKP && pts < min_score) min_score = pts;
		if (pts < min_score_per_position.scores[position])
			min_score_per_position.scores[position] = pts;
	}
	if (surplus_defenders <= 1)
		min_score_per_position.scores[DEF] = min_score;
	if (surplus_midfielders <= 2)
		min_score_per_position.scores[MID] = min_score;
	if (4 - (surplus_defenders + surplus_midfielders) < 2)
		min_score_per_position.scores[FWD] = min_score;
	printf("G: %f D: %f M: %f F: %f\n",
		min_score_per_position.scores[GKP],
		min_score_per_position.scores[DEF],
		min_score_per_position.scores[MID],
		min_score_per_position.scores[FWD]
	);
	return min_score_per_position;
}

void apply_bitset_transfer(Bitset *bitset, pid transfer_out, pid transfer_in) {
	if (is_bit_set(bitset, transfer_out)) {
		set_bit(bitset, transfer_in);
		clear_bit(bitset, transfer_out);
	}
}

void apply_transfer(ui8 out_idx, pid transfer_out, pid transfer_in) {
	Position position = index_to_position(out_idx);
	balance += players[position][current_squad[out_idx]].cost;
	balance -= players[position][transfer_in].cost;
	tid out_team = players[position][transfer_out].team_id;
	tid in_team = players[position][transfer_in].team_id;
	if (out_team != in_team) {
		team_counts[out_team] = team_counts[out_team] - 1;
		team_counts[in_team] = team_counts[in_team] + 1;
		if (team_counts[out_team] == 2) {
			overrepresented_teams[out_team] = false;
			remove_from_list(overrepresented_team_list, &overrepresented_team_c, out_team);
		}
		if (team_counts[in_team] == 3) {
			overrepresented_teams[in_team] = true;
			overrepresented_team_list[overrepresented_team_c++] = in_team;
		}
	}
	apply_bitset_transfer(&current_squad_bs[position], transfer_out, transfer_in);
	current_squad[out_idx] = transfer_in;
}

pid wildcard_teams[WEEKS_IN_SEASON][SQUAD_SIZE];
Bitset wildcard_teams_bs[WEEKS_IN_SEASON][POSITIONS];
void apply_transfer(ui8 i) {
	Transfer t = transfer_seq[i];
	if (t.transfer_in == WILDCARD) {
		ui16 out_squad_cost = 0;
		for (ui8 j = 0; j < SQUAD_SIZE; ++j)
			out_squad_cost += players[index_to_position(j)][current_squad[j]].cost;
		memcpy(current_squad, wildcard_teams[i], SQUAD_SIZE * sizeof(pid));
		memcpy(current_squad_bs, wildcard_teams_bs[i], POSITIONS * sizeof(Bitset));
		for (ui8 j = 0; j < TEAMS; ++j) {
			overrepresented_teams[j] = false;
			team_counts[j] = 0;
		}
		overrepresented_team_c = 0;
		for (int i = 0; i < POSITIONS; ++i) current_squad_bs[i] = new_bitset();
		ui16 in_squad_cost = 0;
		for (ui8 j = 0; j < SQUAD_SIZE; ++j) {
			Position position = index_to_position(j);
			pid player_id = current_squad[j];
			Player player = players[position][player_id];
			tid team_id = player.team_id;
			in_squad_cost += player.cost;
			set_bit(&current_squad_bs[position], player_id);
			++team_counts[team_id];
			if (team_counts[team_id] == 3) {
				overrepresented_teams[team_id] = true;
				overrepresented_team_list[overrepresented_team_c++] = team_id;
			}
		}
		balance += out_squad_cost;
		balance -= in_squad_cost;
	} else if (t.out_idx != NULL_IDX) apply_transfer(t.out_idx, t.transfer_out, t.transfer_in);
}

typedef struct {
	pid transfer_in: 7;
	ui16 balance: 8;
	ui32 previous;
	bool used_freehit: 1;
	bool used_bench_boost: 1;
	bool used_wildcard: 1;
	bool used_triple_captain: 1;
	bool double_sub: 1;
} TransferState;

typedef struct {
	ui8 a: 4;
	ui8 b: 4;
} OutIDXPair;

vector<TransferState> transfer_tree;
vector<OutIDXPair> transfer_tree2;
bool transfer_tree2_len_even = true;
ui8 get_out_idx(ui32 i) {
	if (i & 1) return transfer_tree2[i >> 1].b;
	return transfer_tree2[i >> 1].a;
}
void add_out_idx(ui8 out_idx) {
	if (transfer_tree2_len_even) transfer_tree2.push_back({out_idx, 0});
	else transfer_tree2[transfer_tree2.size() - 1].b = out_idx;
	transfer_tree2_len_even = !transfer_tree2_len_even;
}
vector<ui32> by_score[WEEKS_IN_SEASON][1 << CHIPS];
vector<ui32> by_balance[WEEKS_IN_SEASON][1 << CHIPS];
unordered_map<ui32, float> state_scores;

struct TransferStateCompare {
	bool operator()(const ui32& a_idx, const ui32& b_idx) const {
		float a_score;
		float b_score;
		if (state_scores.find(a_idx) == state_scores.end()) a_score = 0;
		else a_score = state_scores[a_idx];
		if (state_scores.find(b_idx) == state_scores.end()) b_score = 0;
		else b_score = state_scores[b_idx];
		return a_score < b_score;
	}
};

struct TransferStateCompareBalance {
	bool operator()(const ui32& a_idx, const ui32& b_idx) const {
		TransferState a = transfer_tree[a_idx];
		TransferState b = transfer_tree[b_idx];
		if (a.balance == b.balance) {
			float a_score;
			float b_score;
			if (state_scores.find(a_idx) == state_scores.end()) a_score = 0;
			else a_score = state_scores[a_idx];
			if (state_scores.find(b_idx) == state_scores.end()) b_score = 0;
			else b_score = state_scores[b_idx];
			return a_score < b_score;
		}
		return a.balance < b.balance;
	}
};

ui8 get_chip_index(TransferState ts) {
	ui8 idx = 0;
	idx |= ts.used_freehit;
	idx |= ts.used_wildcard << 1;
	idx |= ts.used_bench_boost << 2;
	idx |= ts.used_triple_captain << 3;
	return idx;
}

ui8 apply_transfers_in_context_squad(TransferState cur, ui8 cur_out_idx) {
	ui8 transfers = 0;
	while (cur.previous != 0xFFFFFFFF) {
		bool used_triple_captain = cur.used_triple_captain;
		if (
			used_triple_captain
			&& cur.previous != 0xFFFFFFFF
			&& transfer_tree[cur.previous].used_triple_captain
		) used_triple_captain = false;
		bool used_bench_boost = cur.used_bench_boost;
		if (
			used_bench_boost
			&& cur.previous != 0xFFFFFFFF
			&& transfer_tree[cur.previous].used_bench_boost
		) used_bench_boost = false;
		transfer_seq[transfers++] = {
			cur_out_idx, 0, cur.transfer_in, used_triple_captain, used_bench_boost,
			cur.double_sub
		};
		cur_out_idx = get_out_idx(cur.previous);
		cur = transfer_tree[cur.previous];
	}
	for (int j = 0; j <= (transfers - 2) / 2; ++j) {
		Transfer t = transfer_seq[j];
		transfer_seq[j] = transfer_seq[transfers - j - 1];
		transfer_seq[transfers - j - 1] = t;
	}
	for (int j = 0; j < SQUAD_SIZE; ++j) context_squad[j] = current_squad[j];
	ui8 depth = 0;
	for (int j = 0; j < transfers; ++j) {
		Transfer t = transfer_seq[j];
		if (t.transfer_in == WILDCARD) {
			transfer_seq[j].transfer_out = NO_TRANSFER;
			memcpy(context_squad, wildcard_teams[depth], SQUAD_SIZE * sizeof(pid));
		} else if (t.out_idx == NULL_IDX) {
			transfer_seq[j].transfer_out = NO_TRANSFER;
		} else {
			transfer_seq[j].transfer_out = context_squad[t.out_idx];
			context_squad[t.out_idx] = t.transfer_in;
		}
		depth += !t.double_sub;
	}
	return transfers;
}

float wildcard_scores[WEEKS_IN_SEASON];
float best_remaining_score_per_gameweek[WEEKS_IN_SEASON];
float best_score_per_gameweek[WEEKS_IN_SEASON];
unordered_map<ui64, float> best_score_per_squad[WEEKS_IN_SEASON][1 << CHIPS];
void get_possible_transfers(
	ui32 i, float previous_score, ui8 depth, float max_pessimistic_score
) {
	TransferState previous = transfer_tree[i];
	ui8 chip_index = get_chip_index(previous);
	ui8 previous_out_idx = get_out_idx(i);
	TransferState prev_prev;
	ui8 prev_prev_out_idx;
	pid transfer_out;
	if (previous_out_idx == NULL_IDX) transfer_out = NO_TRANSFER;
	else transfer_out = current_squad[previous_out_idx];
	if (previous.previous != 0xFFFFFFFF) {
		prev_prev = transfer_tree[previous.previous];
		prev_prev_out_idx = get_out_idx(previous.previous);
	}
	int extra_sub =
		// previous transfer was not skipped.
		previous_out_idx != NULL_IDX
		&& (
			(
				// More than two previous transfers...
				previous.previous != 0
				// Two transfers ago was skipped...
				&& prev_prev_out_idx == NULL_IDX
				// Two transfers ago was not a free-hit chip play...
				&& prev_prev.transfer_in != FREE_HIT
				// Two transfers ago was not a wildcard chip play...
				&& prev_prev.transfer_in != WILDCARD
				// SKIP [T1 T2] <- These two can occur in the same gameweek.
			) || (
				// Only one previous transfer...
				previous.previous == 0
				// Double transfer allowed at the current gameweek.
				&& DOUBLE_TRANSFER
			)
		)
		;
	int triple_captain = !previous.used_triple_captain;
	int bench_boost = !previous.used_bench_boost;
	ui8 transfers = apply_transfers_in_context_squad(previous, previous_out_idx);
	for (int j = 0; j < transfers - 1; ++j) apply_transfer(j);
	BestFormation output;
	float prev_prev_score;
	if (transfers > 0) {
		bool used_bench_boost = transfer_seq[transfers - 1].bench_boost;
		if (used_bench_boost) {
			output.score = 0;
			for (int j = 0; j < SQUAD_SIZE; ++j) {
				Position p = index_to_position(j);
				output.score += player_gameweek_predictions[p][current_squad[j]][depth - 1];
			}
		} else {
			bool used_triple_captain = transfer_seq[transfers - 1].triple_captain;
			output = get_best_formation_score(depth, current_squad, used_triple_captain, 0);
		}
		prev_prev_score = previous_score - output.score;
		apply_transfer(transfers - 1);
	} else prev_prev_score = 0;
	for (int l = 0; l <= extra_sub; ++l) {
		for (ui8 j = 0; j < SQUAD_SIZE; ++j) {
			Position position = index_to_position(j);
			pid player_id =  current_squad[j];
			tid team_id = players[position][player_id].team_id;
			ui16 cost = players[position][player_id].cost;
			bitset_diff(
				&good_candidates[position][depth - l],
				&current_squad_bs[position],
				&candidates
			);
			if (overrepresented_teams[team_id]) {
				for (int k = 0; k < overrepresented_team_c; ++k) {
					tid t = overrepresented_team_list[k];
					if (t != team_id)
						bitset_diff(&candidates, &players_per_team[t][position], &candidates);
				}
			} else {
				for (int k = 0; k < overrepresented_team_c; ++k) bitset_diff(
					&candidates,
					&players_per_team[overrepresented_team_list[k]][position],
					&candidates
				);
			}
			if (l && previous_out_idx != NULL_IDX) clear_bit(&candidates, transfer_out);
			for (int k = 0; k < 2; ++k) if (candidates.bits[k]) for (ui64 m = 0; m < 64L; ++m)
				if (candidates.bits[k] & (1L << m)) {
					pid p = (k << 6) | m;
					if (players[position][p].cost <= balance + cost) {
						for (ui32 q = false; q <= triple_captain; ++q) {
							ui32 n_limit = bench_boost && !q;
							for (ui32 n = false; n <= n_limit; ++n) {
								current_squad[j] = p;
								apply_bitset_transfer(
									&current_squad_bs[position], player_id, p);
								if (n) {
									output.score = 0;
									for (int o = 0; o < SQUAD_SIZE; ++o) {
										Position p = index_to_position(o);
										ui8 idx = current_squad[o];
										output.score +=
											player_gameweek_predictions[p][idx][depth - l];
									}
								} else output = get_best_formation_score(
									depth + 1 - l, current_squad, q, 0
								);
								ui64 h = hash_bitset(current_squad_bs);
								float score;
								if (l) score = prev_prev_score + output.score;
								else score = previous_score + output.score;
								current_squad[j] = player_id;
								apply_bitset_transfer(
									&current_squad_bs[position], p, player_id);
								TransferState next = {
									p, balance, i,
									previous.used_freehit,
									previous.used_bench_boost || n,
									previous.used_wildcard,
									previous.used_triple_captain || q,
									(bool) l
								};
								chip_index = get_chip_index(next);
								if (
									best_score_per_squad[depth + 1 - l][chip_index].find(h) ==
									best_score_per_squad[depth + 1 - l][chip_index].end() ||
									score >= best_score_per_squad[depth + 1 - l][chip_index][h]
								) {
									float optimistic_score =
										score
										+ best_remaining_score_per_gameweek[depth + 1 - l];
									optimistic_score /= games_remaining;
									if (
										previous_out_idx == NULL_IDX ||
										optimistic_score > max_pessimistic_score
									) {
										best_score_per_squad[depth + 1 - l][chip_index][h] =
											score;
										by_score[depth + 1 - l][chip_index].push_back(
											transfer_tree.size()
										);
										by_balance[depth + 1 - l][chip_index].push_back(
											transfer_tree.size()
										);
										state_scores[transfer_tree.size()] = score;
										transfer_tree.push_back(next);
										add_out_idx(j);
										push_heap(
											by_score[depth + 1 - l][chip_index].begin(),
											by_score[depth + 1 - l][chip_index].end(),
											TransferStateCompare()
										);
										push_heap(
											by_balance[depth + 1 - l][chip_index].begin(),
											by_balance[depth + 1 - l][chip_index].end(),
											TransferStateCompareBalance()
										);
									}
								}
							}
						}
					}
				}
		}
	}
	for (ui32 m = false; m <= triple_captain; ++m) {
		ui32 n_limit = bench_boost && !m;
		for (ui32 n = false; n <= n_limit; ++n) {
			if (n) {
				output.score = 0;
				for (int o = 0; o < SQUAD_SIZE; ++o) {
					Position p = index_to_position(o);
					output.score += player_gameweek_predictions[p][current_squad[o]][depth];
				}
			} else output = get_best_formation_score(depth + 1, current_squad, m, 0);
			ui64 h = hash_bitset(current_squad_bs);
			float score = previous_score + output.score;
			TransferState next = {
				NO_TRANSFER, balance, i,
				previous.used_freehit,
				previous.used_bench_boost || n,
				previous.used_wildcard,
				previous.used_triple_captain || m,
				false
			};
			chip_index = get_chip_index(next);
			if (
				best_score_per_squad[depth + 1][chip_index].find(h)
				== best_score_per_squad[depth + 1][chip_index].end()
				|| score >= best_score_per_squad[depth + 1][chip_index][h]
			) best_score_per_squad[depth + 1][chip_index][h] = score;
			float optimistic_score = score + best_remaining_score_per_gameweek[depth + 1];
			optimistic_score /= games_remaining;
			if (optimistic_score > max_pessimistic_score) {
				by_score[depth + 1][chip_index].push_back(transfer_tree.size());
				by_balance[depth + 1][chip_index].push_back(transfer_tree.size());
				state_scores[transfer_tree.size()] = score;
				transfer_tree.push_back(next);
				add_out_idx(NULL_IDX);
				push_heap(
					by_score[depth + 1][chip_index].begin(),
					by_score[depth + 1][chip_index].end(),
					TransferStateCompare()
				);
				push_heap(
					by_balance[depth + 1][chip_index].begin(),
					by_balance[depth + 1][chip_index].end(),
					TransferStateCompareBalance()
				);
			}
		}
	}
	if (!previous.used_freehit) {
		float score = previous_score + best_score_per_gameweek[depth];
		float optimistic_score = score + best_remaining_score_per_gameweek[depth + 1];
		optimistic_score /= games_remaining;
		if (optimistic_score > max_pessimistic_score) {
			TransferState next = {
				FREE_HIT, balance, i,
				true,
				previous.used_bench_boost,
				previous.used_wildcard,
				previous.used_triple_captain,
				false
			};
			chip_index = get_chip_index(next);
			by_score[depth + 1][chip_index].push_back(transfer_tree.size());
			by_balance[depth + 1][chip_index].push_back(transfer_tree.size());
			state_scores[transfer_tree.size()] = score;
			transfer_tree.push_back(next);
			add_out_idx(NULL_IDX);
			push_heap(
				by_score[depth + 1][chip_index].begin(),
				by_score[depth + 1][chip_index].end(),
				TransferStateCompare()
			);
			push_heap(
				by_balance[depth + 1][chip_index].begin(),
				by_balance[depth + 1][chip_index].end(),
				TransferStateCompareBalance()
			);
		}
	}
	if (!previous.used_wildcard) {
		ui64 h = hash_bitset(wildcard_teams_bs[depth]);
		TransferState next = {
			WILDCARD, balance, i,
			previous.used_freehit,
			previous.used_bench_boost,
			true,
			previous.used_triple_captain,
			false
		};
		chip_index = get_chip_index(next);
		float score = previous_score + wildcard_scores[depth];
		if (
			best_score_per_squad[depth][chip_index].find(h)
			== best_score_per_squad[depth][chip_index].end()
			|| score >= best_score_per_squad[depth][chip_index][h]
		) {
			float optimistic_score = score + best_remaining_score_per_gameweek[depth + 1];
			optimistic_score /= games_remaining;
			if (optimistic_score > max_pessimistic_score) {
				best_score_per_squad[depth][chip_index][h] = score;
				chip_index = get_chip_index(next);
				by_score[depth + 1][chip_index].push_back(transfer_tree.size());
				by_balance[depth + 1][chip_index].push_back(transfer_tree.size());
				state_scores[transfer_tree.size()] = score;
				transfer_tree.push_back(next);
				add_out_idx(NULL_IDX);
				push_heap(
					by_score[depth + 1][chip_index].begin(),
					by_score[depth + 1][chip_index].end(),
					TransferStateCompare()
				);
				push_heap(
					by_balance[depth + 1][chip_index].begin(),
					by_balance[depth + 1][chip_index].end(),
					TransferStateCompareBalance()
				);
			}
		}
	}
	memcpy(current_squad, starting_squad, SQUAD_SIZE * sizeof(pid));
	memcpy(current_squad_bs, starting_squad_bs, POSITIONS * sizeof(Bitset));
	balance = starting_balance;
	overrepresented_team_c = starting_overrepresented_team_c;
	memcpy(overrepresented_teams, starting_overrepresented_teams, TEAMS * sizeof(bool));
	memcpy(overrepresented_team_list, starting_overrepresented_team_list,
		(SQUAD_SIZE / 3) * sizeof(tid));
	memcpy(team_counts, starting_team_counts, TEAMS * sizeof(int));
}

bool by_score_empty(int i) {
	for (int j = (1 << CHIPS) - 1; j >= 0; --j) if (by_score[i][j].size() > 0) return false;
	return true;
}

pid context_squad2[SQUAD_SIZE];
void print_transfers(pid *squad, Transfer *transfer_seq, ui8 transfers) {
	for (int i = 0; i < SQUAD_SIZE; ++i) context_squad2[i] = squad[i];
	printf("[");
	int j = 0;
	for (int i = 0; i < transfers; ++i) {
		Transfer t = transfer_seq[i];
		Position p = index_to_position(t.out_idx);
		if (t.transfer_in == NO_TRANSFER) printf("SKIP");
		else if (t.transfer_in == FREE_HIT) printf("FREEHIT");
		else if (t.transfer_in == WILDCARD) {
			printf("**");
			memcpy(context_squad2, wildcard_teams[j], SQUAD_SIZE * sizeof(pid));
		} else {
			printf("%u->%u",
				players[p][context_squad2[t.out_idx]].id,
				players[p][t.transfer_in].id
			);
			context_squad2[t.out_idx] = t.transfer_in;
		}
		if (t.triple_captain) printf("x3");
		if (t.bench_boost) printf("-BB");
		if (t.transfer_in == FREE_HIT) {
			printf("=%0.1f", best_score_per_gameweek[j]);
		} else if (t.bench_boost) {
			float score = 0;
			for (int l = 0; l < SQUAD_SIZE; ++l) {
				Position p = index_to_position(l);
				score += player_gameweek_predictions[p][context_squad2[l]][j];
			}
			printf("=%0.1f", score);
		} else {
			BestFormation best =
				get_best_formation_score(j + 1, context_squad2, t.triple_captain, 0);
			printf("=%0.1f", best.score);
		}
		if (t.double_sub) printf("++");
		else ++j;
		printf(" ");
	}
	printf("]\n");
}

typedef struct {
	float score;
	ui32 i;
	ui32 count;
} ScoredState;

int compare_scored_state(const void *p1, const void *p2) {
  	ScoredState s1 = *(ScoredState*) p1;
	ScoredState s2 = *(ScoredState*) p2;
	if (s1.score > s2.score) return -1;
	if (s1.score < s2.score) return +1;
	return 0;
}

ui8 rand_chars[1 << 16];
ui16 rand_chars_i = 0;
bool rand_chars_initialised = false;
ui8 rand_ui8() {
	if (!rand_chars_initialised) {
		for (int i = 0; i < (1 << 16); ++i) rand_chars[i] = rand() & 0xFF;
		rand_chars_initialised = true;
	}
	return rand_chars[rand_chars_i++];
}

bool similar(TransferState *tree, ui32 a, ui32 b) {
	ui32 prev_a;
	while (tree[a].previous != 0 && tree[a].previous != 0xFFFFFFFF) {
		prev_a = a;
		a = tree[a].previous;
	}
	ui32 prev_b;
	while (tree[b].previous != 0 && tree[b].previous != 0xFFFFFFFF) {
		prev_b = b;
		b = tree[b].previous;
	}
	return prev_a == prev_b;
}

unordered_set<ui32> seen[WEEKS_IN_SEASON];
void f() {
	float max_pessimistic_score[4];
	for (ui8 i = 0; i < 4; ++i) max_pessimistic_score[i] = 0;
	ui32 i = 0;
	ui32 prev_i = 1;
	ui32 prev_j = 1;
	ui32 j = 0;
	bool is_by_score = true;
	float max_end_of_season_score = 0;
	int max_end_of_season_j;
	int iteration = 0;
	vector<ScoredState> best_scores;
	while (by_score[i][j].size() > 0) {
		vector<ui32> (&heap)[WEEKS_IN_SEASON][1 << CHIPS] =
			is_by_score ? by_score : by_balance;
		if (heap[i][j].size() > 0) {
			if (is_by_score)
				pop_heap(heap[i][j].begin(), heap[i][j].end(), TransferStateCompare());
			else pop_heap(heap[i][j].begin(), heap[i][j].end(), TransferStateCompareBalance());
			ui32 last_idx = heap[i][j].size() - 1;
			ui32 k = heap[i][j][last_idx];
			heap[i][j].pop_back();
			if (heap[i][j].size() == 0) {
				if (is_by_score) by_balance[i][j].clear();
				else by_score[i][j].clear();
			}
			if (seen[i].find(k) == seen[i].end()) {
				seen[i].insert(k);
				TransferState state = transfer_tree[k];
				float previous_score = state_scores[k];
				state_scores.erase(k);
				ui8 out_idx = get_out_idx(k);
				ui8 transfers = apply_transfers_in_context_squad(state, out_idx);
				float pessimistic_score = previous_score;
				float mean_next_six = 0;
				for (int r = i + 1; r <= MIN(games_remaining, i + 6); ++r)
					mean_next_six +=
						get_best_formation_score(r, context_squad, false, 0).score;
				mean_next_six /= MIN(games_remaining - i, 6);
				for (int r = i + 1; r <= games_remaining; ++r) {
					pessimistic_score +=
						get_best_formation_score(r, context_squad, false, 0).score;
				}
				pessimistic_score /= games_remaining;
				float realistic_score = previous_score;
				for (int r = i + 1; r <= games_remaining; ++r)
					realistic_score += mean_next_six;
				realistic_score /= games_remaining;
				float mean_score = previous_score / i;
				float unrealistic_score = previous_score;
				unrealistic_score += best_remaining_score_per_gameweek[i];
				unrealistic_score /= games_remaining;
				ui8 chip_index =
					(state.used_triple_captain << 1) |
					state.used_bench_boost;
				float cutoff = max_pessimistic_score[chip_index];
				if (pessimistic_score > cutoff) {
					cutoff = pessimistic_score;
					max_pessimistic_score[chip_index] = cutoff;
					transfers = apply_transfers_in_context_squad(state, out_idx);
					for (int d = 0; d < games_remaining; ++d) {
						ui32 l = 0;
						for (int k = 0; k < by_score[d][j].size(); ++k) {
							ui32 idx = by_score[d][j][k];
							float s = state_scores[idx];
							float optimistic_score = s + best_remaining_score_per_gameweek[d];
							optimistic_score /= games_remaining;
							if (optimistic_score > cutoff) {
								by_score[d][j][l++] = idx;
								push_heap(
									by_score[d][j].begin(),
									by_score[d][j].begin() + l,
									TransferStateCompare()
								);
							} else seen[d].insert(idx);
						}
						by_score[d][j].resize(l);
					}
				}
				float score = MIN(mean_score, realistic_score);
				float max_score;
				if (best_scores.size() < 100) max_score = -1;
				else max_score = best_scores[100 - 1].score;
				if (score > max_score) {
					bool done = false;
					bool set = false;
					for (int i = 0; !done && i < MIN(best_scores.size(), 100); ++i) {
						ScoredState scored_state = best_scores[i];
						if (similar(&transfer_tree[0], k, scored_state.i)) {
							set = score > scored_state.score;
							if (set) best_scores[i] = {score, k, scored_state.count + 1};
							done = true;
						}
					}
					if (!done) {
						if (best_scores.size() <= 100) best_scores.push_back({score, k, 1});
						else best_scores[100] = {score, k, 1};
					}
					if (!done || set) {
						qsort(
							&best_scores[0],
							best_scores.size(),
							sizeof(ScoredState),
							compare_scored_state
						);
						printf(
							"pessimist: %f mean: %f (%f/%u) realist: %f optimist: %f gw: %u\n",
							pessimistic_score, mean_score, previous_score, i,
							realistic_score, unrealistic_score, i);
						get_possible_transfers(k, previous_score, i, cutoff);
						for (int i = 0; i < MIN(best_scores.size(), 100); ++i) {
							ScoredState scored_state = best_scores[i];
							printf("\t%0.3fx%u: ", scored_state.score, scored_state.count);
							fflush(stdout);
							TransferState state = transfer_tree[scored_state.i];
							transfers = apply_transfers_in_context_squad(
								state, get_out_idx(scored_state.i)
							);
							print_transfers(current_squad, transfer_seq, transfers);
							fflush(stdout);
						}
					}
				} else {
					float optimistic_score =
						previous_score + best_remaining_score_per_gameweek[i];
					optimistic_score /= games_remaining;
					if (
						(
							state.previous != 0xFFFFFFFF &&
							get_out_idx(state.previous) == NULL_IDX
						) || optimistic_score > cutoff
					) {
						get_possible_transfers(k, previous_score, i, cutoff);
					} else if (is_by_score) {
						by_score[i][j].clear();
						by_balance[i][j].clear();
					}
				}
				if (i == games_remaining - 1) {
					if (mean_score > max_end_of_season_score) {
						max_end_of_season_score = mean_score;
						max_end_of_season_j = k;
					}
				}
			}
		}
		if (i <= 2 && !(by_score_empty(2) && by_score_empty(1) && by_score_empty(0))) {
			do {
				i = rand_ui8() % 3;
				j = (j + 1) & ((1 << CHIPS) - 1);
			} while (by_score[i][j].size() == 0);
		} else {
			int k = 0;
			while (k < games_remaining && by_score_empty(k)) ++k;
			if (k < games_remaining) {
				do {
					i = rand_ui8() % games_remaining;
					j = rand_ui8() & ((1 << CHIPS) - 1);
				} while (by_score[i][j].size() == 0);
				is_by_score = rand_ui8() & 1;
			}
		}
	}
}

ui8 tc[TEAMS];

float h1(float pts, ui16 cost) {
	return pts;
}

float h2(float pts, ui16 cost) {
	return pts / cost;
}

typedef float (*scoring_function)(float, ui16);

ui16 min_cost_per_position[POSITIONS];

Bitset dream_team_bs[POSITIONS];
ui16 max_cost_per_position[POSITIONS];
void fill_wildcard_transfers(
	float sum, ui16 balance, float *best_score, ui8 offset, ui8 lo, ui8 hi
) {
	float score = get_best_formation_score(lo, dream_squad, false, 0).score;
	best_scores[lo - 1] = score;
	sum += score;
	if (lo == hi) {
		ui8 total = hi - offset + 1;
		sum /= total;
		if (sum > *best_score) {
			for (int i = transfer_seq_l - 1; i >= 0; --i) {
				int j = transfer_seq_l - 1 - i;
				float score = get_best_formation_score(lo - j, dream_squad, false, 0).score;
				Transfer t = transfer_seq[i];
				dream_squad[t.out_idx] = t.transfer_out;
			}
			float score = get_best_formation_score(1, dream_squad, false, 0).score;
			*best_score = sum;
			for (int i = 0; i < SQUAD_SIZE; ++i) best_dream_squad[i] = dream_squad[i];
			for (int i = 0; i < transfer_seq_l; ++i) best_transfer_seq[i] = transfer_seq[i];
			best_transfer_seq_l = transfer_seq_l;
			for (int i = 0; i < transfer_seq_l; ++i) {
				Transfer t = transfer_seq[i];
				dream_squad[t.out_idx] = t.transfer_in;
			}
		}
	} else {
		for (ui16 i = 0; i < players_by_score_l; ++i) {
			PlayerID transfer_in_id = players_by_score[lo - offset][i];
			Position p = transfer_in_id.position;
			if (is_bit_set(&dream_team_bs[p], transfer_in_id.i)) continue;
			// TODO delete this... Rice injured this week only.
			if (transfer_in_id.i == 30) continue;
			Player transfer_in = players[p][transfer_in_id.i];
			if (transfer_in.taxed_cost > max_cost_per_position[p] + balance) continue;
			tid t_in = transfer_in.team_id;
			// Iterate through each player at this position
			// in the dream squad...
			for (
				ui8 out_idx = POSITION_OFFSETS[p][0];
				out_idx <= POSITION_OFFSETS[p][1];
				++out_idx
			) {
				pid transfer_out_id = dream_squad[out_idx];
				Player transfer_out = players[p][transfer_out_id];
				if (transfer_in.taxed_cost > transfer_out.taxed_cost + balance) continue;
				tid t_out = transfer_out.team_id;
				if (t_in != t_out && tc[t_in] == 3) continue;
				Transfer t = {out_idx, transfer_out_id, transfer_in_id.i, false, false};

				balance +=
					((short) transfer_out.taxed_cost) - ((short) transfer_in.taxed_cost);
				transfer_seq[transfer_seq_l] = t;
				++transfer_seq_l;
				dream_squad[out_idx] = transfer_in_id.i;
				clear_bit(&dream_team_bs[p], transfer_out_id);
				set_bit(&dream_team_bs[p], transfer_in_id.i);
				++tc[t_in];
				--tc[t_out];

				fill_wildcard_transfers(sum, balance, best_score, offset, lo + 1, hi);

				balance +=
					((short) transfer_in.taxed_cost) - ((short) transfer_out.taxed_cost);
				dream_squad[out_idx] = transfer_out_id;
				clear_bit(&dream_team_bs[p], transfer_in_id.i);
				set_bit(&dream_team_bs[p], transfer_out_id);
				--transfer_seq_l;
				--tc[t_in];
				++tc[t_out];
			}
		}
	}
}

void fill_wildcard(
	char wildcard_transfers_remaining,
	ui16 balance, ui16 i, float *best_score, ui8 *offsets, ui8 lo, ui8 hi,
	PositionScores min_score_per_position
) {
	float best_possible = 0;
	ui16 min_tail_cost = 0;
	if (wildcard_transfers_remaining < 0) return;
	for (int p = GKP; p <= FWD; ++p) min_tail_cost +=
		min_cost_per_position[p] * (POSITION_OFFSETS[p][1] + 1 - offsets[p]);
	if (balance < min_tail_cost) return;
	PlayerID player;
	for (ui8 p = GKP; p <= FWD; ++p) {
		ui16 k = i;
		ui8 o = 0;
		for (ui8 offset = offsets[p]; offset <= POSITION_OFFSETS[p][1]; ++offset) {
			// Find a player not in the dream squad...
			while (k < players_by_score_l) {
				player = players_by_score[0][k++];
				Position pos = player.position;
				if (pos != p) continue;
				ui8 l = POSITION_OFFSETS[pos][0];
				while (l < POSITION_OFFSETS[pos][1])
					if (dream_squad[l++] == player.i) break;
				// If dream squad does NOT contains the player...
				if (l == POSITION_OFFSETS[pos][1]) break;
			}
			if (k == players_by_score_l) return;
			default_pts_per_position[p][o++] = player.i;
		}
	}
	best_possible += get_best_formation_score(lo, dream_squad, false, 0).score;
	for (ui8 j = lo + 1; j <= hi; ++j) {
		ui8 transfers = j - lo;
		PlayerID player;
		for (ui8 p = GKP; p <= FWD; ++p) {
			ui16 k = i;
			ui8 o = 0;
			for (ui8 offset = offsets[p]; offset <= POSITION_OFFSETS[p][1]; ++offset) {
				while (k < players_by_score_l) {
					player = players_by_score[transfers][k++];
					Position pos = player.position;
					if (pos != p) continue;
					ui8 l = POSITION_OFFSETS[pos][0];
					while (l < POSITION_OFFSETS[pos][1])
						if (dream_squad[l++] == player.i) break;
					if (l == POSITION_OFFSETS[pos][1]) break;
				}
				if (k == players_by_score_l) return;
				default_pts_per_position[p][o++] = player.i;
			}
		}
		float score = get_best_formation_score(j, dream_squad, false, transfers).score;
		best_possible  += score;
	}
	best_possible /= (hi - lo + 1);
	if (best_possible * 1.022 < *best_score) return;
	for (; i < players_by_score_l; ++i) {
		PlayerID p = players_by_score[0][i];
		bool ignore = false;
		for (int j = 0; !ignore && j < CONSTANTS_L; ++j)
			ignore = p.i == CONSTANTS[j].i && p.position == CONSTANTS[j].position;
		if (ignore) continue;
		bool is_transfer = true;
		for (
			int j = POSITION_OFFSETS[p.position][0];
			is_transfer && j <= POSITION_OFFSETS[p.position][1];
			++j
		) is_transfer = p.i != starting_squad[j];
		char next_wildcard_transfers_remaining;
		if (is_transfer)
			next_wildcard_transfers_remaining = wildcard_transfers_remaining - 1;
		else next_wildcard_transfers_remaining = wildcard_transfers_remaining;
		Player player = players[p.position][p.i];
		if (
			//player.id == 55 || // Timber
			//player.id == 40 ||
			//player.id == 32 ||
			//player.id == 542 ||
			//player.id == 186 ||
			//player.id == 108 ||
			//player.id == 319 || // Collins warned.
			false
		) continue; // J.Timber and Trossard injured.
		tid t = player.team_id;
		if (tc[t] == 3 || player.taxed_cost > balance) continue;
		// Player's predicted score not good enough.
		if (
			player_gameweek_predictions[p.position][p.i][lo - 1] <
			min_score_per_position.scores[p.position]
		) {
			int p_i = POSITION_OFFSETS[p.position][0];
			for (; p_i <= POSITION_OFFSETS[p.position][1]; ++p_i)
				if (current_squad[p_i] == p.i) break;
			// Skip this player when they are in the current
			// squad (if their points are good enough to be in
			// the current squad we don't skip either).
			if (p_i > POSITION_OFFSETS[p.position][1]) {
				continue;
			}
		}
		if (offsets[p.position] > POSITION_OFFSETS[p.position][1]) continue;
		dream_squad[offsets[p.position]] = p.i;
		++offsets[p.position];
		++tc[t];
		fill_wildcard(
			next_wildcard_transfers_remaining,
			balance - player.taxed_cost, i + 1, best_score, offsets, lo, hi,
			min_score_per_position
		);
		--tc[t];
		--offsets[p.position];
		dream_squad[offsets[p.position]] = NO_TRANSFER;
	}
	ui8 pos;
	for (pos = GKP; pos <= FWD; ++pos)
		if (offsets[pos] <= POSITION_OFFSETS[pos][1]) break;
	if (pos > FWD) {
		for (ui8 i = GKP; i <= FWD; ++i) {
			dream_team_bs[i] = new_bitset();
			max_cost_per_position[i] = 0;
		}
		for (ui8 i = 0; i < SQUAD_SIZE; ++i) {
			Position p = index_to_position(i);
			pid idx = dream_squad[i];
			set_bit(&dream_team_bs[p], idx);
			Player player = players[p][idx];
			if (player.taxed_cost > max_cost_per_position[p])
				max_cost_per_position[p] = player.taxed_cost;
		}
		fill_wildcard_transfers(0, balance, best_score, lo, lo, hi);
	}
}

int main() {
	signal(SIGINT, exit_handler);
	TransferState INITIAL_STATE = {
		NO_TRANSFER, 0, 0xFFFFFFFF, USED_FREEHIT, USED_BENCHBOOST, USED_WILDCARD, USED_TRIPLE
	};
	transfer_tree.push_back(INITIAL_STATE);
	add_out_idx(NULL_IDX);
	by_score[0][0].push_back(0);
	by_balance[0][0].push_back(0);

	FILE *player_costs_f = fopen("data/bin/player_costs.bin", "rb");
	FILE *player_teams_f = fopen("data/bin/player_teams.bin", "rb");
	FILE *player_positions_f = fopen("data/bin/player_positions.bin", "rb");
	struct stat st;
	stat("data/bin/player_positions.bin", &st);
	ui32 tmp_players_l = st.st_size;
	for (int i = 0; i < POSITIONS; ++i) min_cost_per_position[i] = 0xFFFF;
	Player tmp_players[2000];
	for (ui16 i = 0; i < tmp_players_l; ++i) {
		ui16 cost = (ui16) (read_float(player_costs_f) * 10 + 0.1);
		tmp_players[i].cost = cost;
		tmp_players[i].taxed_cost = cost;
		tmp_players[i].team_id = read_char(player_teams_f);
		Position position = (Position) read_char(player_positions_f);
		tmp_players[i].position = position;
		min_cost_per_position[position] = MIN(min_cost_per_position[position], cost);
		tmp_players[i].id = i;
		if (i == 36) ASTON_VILLA = tmp_players[i].team_id;
		if (i == 5) MANU = tmp_players[i].team_id;
		if (i == 0) MAN_CITY = tmp_players[i].team_id;
		if (i == 38) BRENTFORD = tmp_players[i].team_id;
		if (i == 4) ARSENAL = tmp_players[i].team_id;
		if (USE_CONSTANTS) {
			if (
				false
				// Dúbravka
				|| i == 640
				// Timber
				//|| i == 56
				// Haaland
				|| i == 0
				// Saka
				//|| i == 4
				// Foden
				//|| i == 7
				// Semenyo
				//|| i == 20
				// Konaté
				//|| i == 174
				// Becker
				//|| i == 168
				// Jiminez
				//|| i == 73
				// Thiago
				//|| i == 38
				// Szoboszlai
				//|| i == 48
			   || false
			) {
				CONSTANTS[CONSTANTS_L++] = {position, i};
			}
		}
	}
	for (int i = 0; i < POSITIONS; ++i) players_l[i] = 0;
	fclose(player_costs_f);
	fclose(player_positions_f);
	fclose(player_teams_f);

	for (int i = 0; i < POSITIONS; ++i) bargain_players[i] = new_bitset();
	for (int i = 0; i < POSITIONS; ++i) current_squad_bs[i] = new_bitset();
	for (int j = 0; j < games_remaining; ++j)
		for (int i = 0; i < POSITIONS; ++i) wildcard_teams_bs[j][i] = new_bitset();

	FILE *good_players_f = fopen("data/bin/good_players.bin", "rb");
	games_remaining = read_char(good_players_f);
	for (int i = 0; i < POSITIONS; ++i)
		good_candidates[i] = (Bitset*) malloc(games_remaining * sizeof(Bitset));

	FILE *player_gameweek_predictions_f =
		fopen("data/bin/player_gameweek_predictions.bin", "rb");
	float tmp_player_gameweek_predictions[2000][WEEKS_IN_SEASON];
	
	for (int i = 0; i < tmp_players_l; ++i) {
		for (int j = 0; j < games_remaining; ++j) {
			float prediction = read_float(player_gameweek_predictions_f);
			tmp_player_gameweek_predictions[i][j] = prediction;
		}
	}

	PlayerID player_mapping[tmp_players_l];
	for (int i = 0; i < tmp_players_l; ++i) player_mapping[i] = {GKP, NO_TRANSFER};
	FILE *current_squad_f = fopen("data/bin/current_squad.bin", "rb");
	balance = (ui16) (read_float(current_squad_f) * 10 + 0.1);
	printf("Current balance: %u\n", balance);
	starting_balance = balance;
	int offsets[POSITIONS] = {GKP1, DEF1, MID1, FWD1};
	for (int i = 0; i < SQUAD_SIZE; ++i) {
		pid tmp_player_id = read_short(current_squad_f);
		printf("T: %u ", tmp_player_id);
		ui16 paid_cost = read_short(current_squad_f);
		if (player_mapping[tmp_player_id].i == NO_TRANSFER) {
			Position pos = tmp_players[tmp_player_id].position;
			pid idx = players_l[pos];
			player_mapping[tmp_player_id] = {pos, idx};
			players[pos][idx] = tmp_players[tmp_player_id];
			for (int i = 0; i < games_remaining; ++i)
				player_gameweek_predictions[pos][idx][i] =
					tmp_player_gameweek_predictions[tmp_player_id][i];
			players_l[pos] = idx + 1;
		}
		Position position = player_mapping[tmp_player_id].position;
		pid idx = player_mapping[tmp_player_id].i;
		current_squad[offsets[position]++] = idx;
		ui16 taxed_cost;
		Player *player = &players[position][idx];
		if (paid_cost < player->cost) taxed_cost = (player->cost + paid_cost) >> 1;
		else taxed_cost = player->cost;
		player->taxed_cost = taxed_cost;
		tid team_id = player->team_id;
		set_bit(&current_squad_bs[position], idx);
		++team_counts[team_id];
   		if (team_counts[team_id] == 3) {
       		overrepresented_teams[team_id] = true;
       		overrepresented_team_list[overrepresented_team_c++] = team_id;
		}
		printf(
			"Cost: %u Taxed: %u\n", player->cost, player->taxed_cost);
		team_value += taxed_cost;
	}
	
	unordered_set<tid> worse_in_teams;
	vector<scoring_function> SCORING_FUNCTIONS = {h1, h2};
	PlayerID best_quality_squad[11];
	PlayerID best_bargain_squad[11];
	for (ui8 i = 0; i < WEEKS_IN_SEASON; ++i) best_remaining_score_per_gameweek[i] = 0;
	for (ui8 i = 0; i < TEAMS; ++i) tc[i] = 0;
	for (ui8 gameweek = 1; gameweek <= games_remaining; ++gameweek) {
		players_by_score_l = 0;
		for (scoring_function h : SCORING_FUNCTIONS) {
			for (int p1 = 0; p1 < tmp_players_l; ++p1) {
				worse_in_teams.clear();
				int worse_in_many_ways = 0;
				int worse_in_many_ways_within_team = 0;
				ui16 p1_cost = tmp_players[p1].cost;
				Position p1_pos = tmp_players[p1].position;
				float p1_pts = tmp_player_gameweek_predictions[p1][gameweek - 1];
				tid p1_team = tmp_players[p1].team_id;
				for (int p2 = 0; p2 < tmp_players_l; ++p2) {
					if (p1 == p2) continue;
					float p2_pts = tmp_player_gameweek_predictions[p2][gameweek - 1];
					Position p2_pos = tmp_players[p2].position;
					tid p2_team = tmp_players[p2].team_id;
					if (p1_pos != p2_pos) continue;
					if (p1_cost >= tmp_players[p2].cost && p1_pts < p2_pts) {
						++worse_in_many_ways;
						if (p1_team == p2_team) ++worse_in_many_ways_within_team;
						else worse_in_teams.insert(p2_team);
					}
				}
				bool valid_candidate =
					((int) (worse_in_teams.size() - ((SQUAD_SIZE - 1) / 3))
					+ worse_in_many_ways_within_team)
					< MIN((int) SQUAD_MAKEUP[p1_pos], SQUAD_SIZE - ((SQUAD_SIZE - 1) / 3) * 3);
				if (valid_candidate && player_mapping[p1].i == NO_TRANSFER) {
					pid idx = players_l[p1_pos];
					player_mapping[p1] = {p1_pos, idx};
					players[p1_pos][idx] = tmp_players[p1];
					for (int i = 0; i < games_remaining; ++i)
						player_gameweek_predictions[p1_pos][idx][i] =
							tmp_player_gameweek_predictions[p1][i];
					players_l[p1_pos] = idx + 1;
				}
			}
		}
	}
	for (int i = 0; i < CONSTANTS_L; ++i) {
		PlayerID p = player_mapping[CONSTANTS[i].i];
		CONSTANTS[i].i = p.i;
	}

	FILE *team_players_f = fopen("data/bin/players_per_team.bin", "rb");
	for (ui8 team_id = 0; team_id < TEAMS; ++team_id)
		for (ui8 p = GKP; p <= FWD; ++p) {
			players_per_team[team_id][p] = new_bitset();
			for (int i = read_char(team_players_f); i > 0; --i) {
				ui16 candidate = read_short(team_players_f);
				PlayerID player = player_mapping[candidate];
				if (player.i != NO_TRANSFER) set_bit(&players_per_team[team_id][p], player.i);
			}
		}
	fclose(team_players_f);

	memcpy(starting_squad, current_squad, SQUAD_SIZE * sizeof(pid));
	memcpy(starting_squad_bs, current_squad_bs, POSITIONS * sizeof(Bitset));
	printf("Team value: %u\n", team_value);
	starting_overrepresented_team_c = overrepresented_team_c;
	memcpy(starting_overrepresented_teams, overrepresented_teams, TEAMS * sizeof(bool));
	memcpy(starting_overrepresented_team_list, overrepresented_team_list,
		(SQUAD_SIZE / 3) * sizeof(tid));
	memcpy(starting_team_counts, team_counts, TEAMS * sizeof(int));

	FILE *bargain_players_f = fopen("data/bin/bargain_players.bin", "rb");
	for (ui8 p = GKP; p <= FWD; ++p)
		for (int i = read_short(bargain_players_f); i > 0; --i) {
			ui16 candidate = read_short(bargain_players_f);
			PlayerID player = player_mapping[candidate];
			if (player.i != NO_TRANSFER) set_bit(&bargain_players[p], player.i);
		}
	fclose(bargain_players_f);

	for (int i = 0; i < games_remaining; ++i) {
		for (int j = 0; j < POSITIONS; ++j) {
			ui16 good_candidates_c = read_short(good_players_f);
			good_candidates[j][i] = new_bitset();
			for (int k = 0; k < good_candidates_c; ++k) {
				ui16 candidate = read_short(good_players_f);
				PlayerID player = player_mapping[candidate];
				if (player.i != NO_TRANSFER) set_bit(&good_candidates[j][i], player.i);
			}
			bitset_union(
				&good_candidates[j][i],
				&bargain_players[j],
				&good_candidates[j][i]
			);
		}
	}
	fclose(good_players_f);

	printf("----------------\n");
	for (int i = 0; i < POSITIONS; ++i) {
		printf("%s: %u\n", POSITION_LABELS[i], players_l[i]);
	}
	players_by_score_l = 0;
	for (ui8 position = GKP; position <= FWD; ++position)
		for (pid p1 = 0; p1 < players_l[position]; ++p1) {
			for (int i = 0; i <= WILDCARD_LOOKAHEAD; ++i)
				players_by_score[i][players_by_score_l] = {(Position) position, p1};
			++players_by_score_l;
		}
	printf("PRE:\n");
	print_squad(starting_squad, 1);
	printf("Games remaining: %u\n", games_remaining);
	fflush(stdout);
	FILE *ideal_scores;
	//goto skip_this;
	if ((ideal_scores = fopen("data/bin/ideal_gameweek_scores.bin", "rb")))
		for (ui8 gameweek = 1; gameweek <= games_remaining; ++gameweek) {
			float best_score = read_float(ideal_scores);
			best_score_per_gameweek[gameweek - 1] = best_score;
			printf("GW%d:\t%f\n",
				gameweek + (WEEKS_IN_SEASON - games_remaining), best_score);
			for (int i = 0; i < gameweek; ++i)
				best_remaining_score_per_gameweek[i] += best_score;
		}
    else {
		ideal_scores = fopen("data/bin/ideal_gameweek_scores.bin", "wb");
		for (ui8 gameweek = 1; gameweek <= games_remaining; ++gameweek) {
			gameweek_lo = gameweek;
			gameweek_hi = gameweek;
			PositionScores min_score_per_position =
				get_best_formation_cutoffs_per_position(1, current_squad, false, 0);
			ui8 offsets[POSITIONS] = {GKP1, DEF1, MID1, FWD1};
			ui16 remaining_value = team_value;
			for (ui8 i = 0; i < SQUAD_SIZE; ++i) dream_squad[i] = NO_TRANSFER;
			for (ui8 i = 0; i < TEAMS; ++i) tc[i] = 0;
			// TODO constants.
			for (ui8 i = 0; i < CONSTANTS_L; ++i) {
				PlayerID p = CONSTANTS[i];
				remaining_value -= players[p.position][p.i].taxed_cost;
				dream_squad[offsets[p.position]] = p.i;
				set_bit(&dream_team_bs[p.position], p.i);
				best_dream_squad[offsets[p.position]] = p.i;
				++offsets[p.position];
				++tc[players[p.position][p.i].team_id];
				printf("P: %u\n", players[p.position][p.i].id);
			}
			qsort(
				players_by_score[0],
				players_by_score_l,
				sizeof(PlayerID),
				compare_player_id
			);
			float best_score = 0;
			printf("Remaining: %u\n", remaining_value + balance);
			fill_wildcard(
				WILDCARD_TRANSFERS,
				remaining_value + balance, 0, &best_score, offsets, gameweek, gameweek,
				min_score_per_position
			);
			// TODO constants.
			offsets[GKP] = GKP1;
			offsets[DEF] = DEF1;
			offsets[MID] = MID1;
			offsets[FWD] = FWD1;
			for (ui8 i = 0; i < CONSTANTS_L; ++i) {
				PlayerID p = CONSTANTS[i];
				best_dream_squad[offsets[p.position]++] = p.i;
			}
			ui16 value = 0;
			ui16 taxed_value = 0;
			for (int i = 0; i < SQUAD_SIZE; ++i) {
				value += players[index_to_position(i)][best_dream_squad[i]].cost;
				taxed_value += players[index_to_position(i)][best_dream_squad[i]].taxed_cost;
			}
			for (int i = 0; i < gameweek; ++i)
				best_remaining_score_per_gameweek[i] += best_score;
			best_score_per_gameweek[gameweek - 1] = best_score;
			print_squad(best_dream_squad, gameweek);
			printf(
				"GW%d:\t%f [COST: %u AFTER TAX: %u]\n",
				gameweek + (WEEKS_IN_SEASON - games_remaining), best_score,
				value, taxed_value
			);
			fflush(stdout);
			fwrite(&best_score, sizeof(float), 1, ideal_scores);
		}
	}
	fclose(ideal_scores);
	skip_this:
	if (!USED_WILDCARD) {
		if ((ideal_wildcards = fopen("data/bin/ideal_wildcards.bin", "rb"))) {
			for (ui8 gameweek = 1; gameweek <= games_remaining; ++gameweek) {
				for (int i = 0; i < SQUAD_SIZE; ++i) {
					pid p = read_short(ideal_wildcards);
					wildcard_teams[gameweek - 1][i] = p;
					set_bit(&wildcard_teams_bs[gameweek - 1][index_to_position(i)], p);
				}
				print_squad(wildcard_teams[gameweek - 1], gameweek);
				wildcard_scores[gameweek - 1] = read_float(ideal_wildcards);
				printf("GW%d*:\t%f\n", gameweek + (WEEKS_IN_SEASON - games_remaining),
					wildcard_scores[gameweek - 1]);
				fflush(stdout);
			}
		} else {
			ideal_wildcards = fopen("data/bin/ideal_wildcards.bin", "wb");
			for (ui8 gameweek = 1; gameweek <= games_remaining; ++gameweek) {
				PositionScores min_score_per_position =
					get_best_formation_cutoffs_per_position(1, current_squad, false, 0);
				ui8 lo = gameweek;
				ui8 hi = MIN(gameweek + WILDCARD_LOOKAHEAD, games_remaining);
				ui8 offsets[POSITIONS] = {GKP1, DEF1, MID1, FWD1};
				ui16 remaining_value = team_value;
				for (ui8 i = 0; i < SQUAD_SIZE; ++i) dream_squad[i] = NO_TRANSFER;
				for (ui8 i = 0; i < TEAMS; ++i) tc[i] = 0;
				// TODO constants.
				for (ui8 i = 0; i < CONSTANTS_L; ++i) {
					PlayerID p = CONSTANTS[i];
					remaining_value -= players[p.position][p.i].taxed_cost;
					dream_squad[offsets[p.position]] = p.i;
					set_bit(&dream_team_bs[p.position], p.i);
					best_dream_squad[offsets[p.position]] = p.i;
					++offsets[p.position];
					++tc[players[p.position][p.i].team_id];
				}
				for (int i = 0; i <= WILDCARD_LOOKAHEAD; ++i) {
					gameweek_lo = lo + i;
					gameweek_hi = hi;
					qsort(
						players_by_score[i],
						players_by_score_l,
						sizeof(PlayerID),
						compare_player_id
					);
				}
				float best_score = 0;
				printf("Starting...\n");
				fill_wildcard(
					WILDCARD_TRANSFERS,
					remaining_value + balance, 0, &best_score, offsets, lo, hi,
					min_score_per_position
				);
				// TODO constants.
				offsets[GKP] = GKP1;
				offsets[DEF] = DEF1;
				offsets[MID] = MID1;
				offsets[FWD] = FWD1;
				for (ui8 i = 0; i < CONSTANTS_L; ++i) {
					PlayerID p = CONSTANTS[i];
					best_dream_squad[offsets[p.position]++] = p.i;
				}
				for (int i = 0; i < SQUAD_SIZE; ++i) {
					pid p = best_dream_squad[i];
					wildcard_teams[gameweek - 1][i] = p;
					set_bit(&wildcard_teams_bs[gameweek - 1][index_to_position(i)], p);
					fwrite(&p, sizeof(pid), 1, ideal_wildcards);
				}
				ui16 value = 0;
				ui16 taxed_value = 0;
				for (int i = 0; i < SQUAD_SIZE; ++i) {
					value += players[index_to_position(i)][best_dream_squad[i]].cost;
					taxed_value +=
						players[index_to_position(i)][best_dream_squad[i]].taxed_cost;
				}
				print_squad(wildcard_teams[gameweek - 1], gameweek);
				printf("TRANSFERS: %u\n", best_transfer_seq_l);
				for (int i = 0; i < best_transfer_seq_l; ++i) {
					Transfer t = best_transfer_seq[i];
					printf("OUT -> %u\n", players[index_to_position(t.out_idx)][t.transfer_out].id);
					printf("IN -> %u\n", players[index_to_position(t.out_idx)][t.transfer_in].id);
				}
				printf(
					"GW%d*:\t%f [COST: %u AFTER TAX: %u]\n",
					gameweek + (WEEKS_IN_SEASON - games_remaining),
					best_score,
					value, taxed_value
				);
				BestFormation best =
					get_best_formation_score(gameweek, best_dream_squad, false, 0);
				wildcard_scores[gameweek - 1] = best.score;
				fwrite(&best.score, sizeof(float), 1, ideal_wildcards);
				exit(0);
			}
		}
		fclose(ideal_wildcards);
		ideal_wildcards = NULL;
	}
	exit(0);
	f();

	printf("%f is the best predicted score.\n", best_score);
	for (int i = 0; i < 3; ++i) {
		Transfer t = best_transfer_seq[i];
		ui8 out = t.out_idx;
		pid in = t.transfer_in;
		printf("\t(%u, %u)\n", out, in); fflush(stdout);
		if (t.out_idx != NULL_IDX) current_squad[t.out_idx] = t.transfer_in;
		BestFormation output = get_best_formation_score(i + 1, current_squad, false, 0);
		float score = output.score;
		printf("%f\n", score);
	}
}
