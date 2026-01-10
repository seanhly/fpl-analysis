import numpy as np
import pandas as pd

TEAMS = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Leeds",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Tottenham",
    "Sunderland",
    "West Ham",
    "Wolverhampton Wanderers",
]

GAMES = [
    ("Arsenal", 2.74, 0.16, "Leeds"),
    ("Arsenal", 2.88, 0.29, "Nottingham Forest"),
    ("Aston Villa", 0.32, 1.40, "Newcastle United"),
    ("Aston Villa", 1.21, 2.60, "Crystal Palace"),
    ("Bournemouth", 1.44, 0.62, "Brighton"),
    ("Bournemouth", 1.78, 0.37, "Wolverhampton Wanderers"),
    ("Brentford", 1.13, 0.98, "Aston Villa"),
    ("Brentford", 1.18, 0.76, "Chelsea"),
    ("Brighton", 1.40, 1.19, "Tottenham"),
    ("Brighton", 1.44, 0.90, "Fulham"),
    ("Brighton", 2.21, 2.13, "Manchester City"),
    ("Burnley", 0.17, 2.79, "Liverpool"),
    ("Burnley", 1.00, 1.12, "Sunderland"),
    ("Burnley", 1.14, 0.83, "Nottingham Forest"),
    ("Chelsea", 1.37, 1.03, "Crystal Palace"),
    ("Chelsea", 2.43, 0.74, "Fulham"),
    ("Crystal Palace", 1.10, 1.33, "Nottingham Forest"),
    ("Crystal Palace", 1.76, 0.35, "Sunderland"),
    ("Everton", 1.80, 2.08, "Brighton"),
    ("Everton", 1.89, 0.35, "Aston Villa"),
    ("Fulham", 1.14, 0.83, "Leeds"),
    ("Fulham", 1.65, 1.55, "Manchester United"),
    ("Leeds", 0.68, 0.30, "Newcastle United"),
    ("Leeds", 2.38, 0.67, "Everton"),
    ("Liverpool", 0.48, 0.49, "Arsenal"),
    ("Liverpool", 1.06, 0.72, "Everton"),
    ("Liverpool", 2.33, 1.57, "Bournemouth"),
    ("Manchester City", 1.25, 1.28, "Tottenham"),
    ("Manchester City", 2.00, 1.52, "Manchester United"),
    ("Manchester United", 1.34, 0.47, "Chelsea"),
    ("Manchester United", 1.38, 1.33, "Arsenal"),
    ("Manchester United", 4.02, 1.33, "Burnley"),
    ("Newcastle United", 1.19, 0.38, "Wolverhampton Wanderers"),
    ("Newcastle United", 1.96, 0.65, "Liverpool"),
    ("Nottingham Forest", 0.72, 2.24, "West Ham"),
    ("Nottingham Forest", 1.76, 1.33, "Brentford"),
    ("Sunderland", 0.72, 0.56, "West Ham"),
    ("Sunderland", 1.57, 1.45, "Brentford"),
    ("Tottenham", 0.17, 2.12, "Bournemouth"),
    ("Tottenham", 1.98, 0.73, "Burnley"),
    ("West Ham", 0.47, 2.34, "Crystal Palace"),
    ("West Ham", 0.79, 1.51, "Tottenham"),
    ("West Ham", 0.98, 3.95, "Chelsea"),
    ("Wolverhampton Wanderers", 0.52, 2.30, "Manchester City"),
    ("Wolverhampton Wanderers", 0.94, 2.04, "Everton"),
    ("Wolverhampton Wanderers", 1.57, 0.46, "Leeds"),
]

duplicate_links = {}

for a in TEAMS:
    duplicate_links[a] = {}
    for b in TEAMS:
        if b == a: continue
        duplicate_links[a][b] = 0.01;

for home, home_score, away_score, away in GAMES:
    """
    duplicate_links[away][home] += home_score
    duplicate_links[home][away] += away_score
    """
    """
    diff = home_score - away_score
    if diff > 0:
        duplicate_links[away][home] += diff
    else:
        duplicate_links[home][away] -= -diff
    """
    """
    duplicate_links[away][home] += home_score / (home_score + away_score)
    duplicate_links[home][away] += away_score / (home_score + away_score)
    """
    if home_score > away_score:
        duplicate_links[away][home] += home_score / (home_score + away_score)
    else:
        duplicate_links[home][away] += away_score / (home_score + away_score)

links = [
    (a, b, score)
    for a, row in duplicate_links.items()
    for b, score in row.items()
]

# Extract unique teams (nodes)
teams = list(set([team for edge in links for team in edge[:2]]))
teams.sort()

# Create a dictionary to map teams to indices
team_to_index = {team: idx for idx, team in enumerate(teams)}

# Initialize the adjacency matrix
n = len(teams)
A = np.zeros((n, n))

# Fill the adjacency matrix with the weights
for from_team, to_team, weight in links:
    i = team_to_index[from_team]
    j = team_to_index[to_team]
    A[i, j] = weight

# PageRank calculation
def pagerank(A, d=0.85, tol=1e-6, max_iter=10000):
    n = A.shape[0]
    # Normalize the matrix to get the probabilities
    out_degree = np.sum(A, axis=1)
    for i in range(n):
        if out_degree[i] != 0:
            A[i] /= out_degree[i]
        else:
            A[i] = np.ones(n) / n  # Handle dangling nodes

    # Initial rank
    PR = np.ones(n) / n
    # Personalization vector (uniform distribution)
    personalization = np.ones(n) / n

    for _ in range(max_iter):
        new_PR = (1 - d) * personalization + d * np.dot(A.T, PR)
        if np.linalg.norm(new_PR - PR, 1) < tol:
            break
        PR = new_PR

    return PR

# Calculate PageRank
pagerank_values = pagerank(A)

# Create a DataFrame to show the results
pagerank_df = pd.DataFrame({
    'Team': teams,
    'PageRank': pagerank_values
})

# Sort by PageRank
pagerank_df = pagerank_df.sort_values(by='PageRank', ascending=False)

# Show results
print(pagerank_df)
