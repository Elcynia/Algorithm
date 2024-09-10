import sys
from collections import Counter
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  N = int(input())
  arr = list(map(int, input().split()))
  team_counts = Counter(arr)
  award_teams = []
  for team, people in team_counts.items():
    if people == 6:
      award_teams.append(team)
  rank = 1
  rankings = {}
  for i in arr:
    if i in award_teams:
      if i not in rankings:
        rankings[i] = []
      rankings[i].append(rank)
      rank += 1
      
  team_scores = {}
  for team in award_teams:
      team_scores[team] = sum(rankings[team][:4]) # 각 팀 상위 4명까지 점수 합산

  # 동점일 경우
  draw_teams = []
  min_score = min(team_scores.values())
  for team, score in team_scores.items():
    if (score == min_score):
      draw_teams.append(team)

  if len(draw_teams) > 1:
      winner = min(draw_teams, key=lambda x: rankings[x][4])
  else:
      winner = draw_teams[0]
  print (winner)