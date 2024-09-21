import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
T = int(input())
for tc in range(T):
  n, k, t, m = map(int, input().split()) # 팀 개수, 문제 수, 나의 팀 ID, 로그 엔트리 수
  teams = [{"scores": [0]*(k+1), "submit_cnt": 0, "last_submitted": 0} for _ in range(n+1)]
  for j in range(m):
    teamId, probNum, score = map(int, input().split()) # 팀 id, 문제 번호, 획득한 점수
    teams[teamId]["scores"][probNum] = max(teams[teamId]["scores"][probNum], score)
    teams[teamId]["submit_cnt"] += 1
    teams[teamId]["last_submitted"] = j
  for team in teams:
    team['total_score'] = sum(team['scores'])
  sorted_teams = sorted(enumerate(teams), key=lambda x: (-x[1]["total_score"], x[1]["submit_cnt"], x[1]["last_submitted"]))
  for rank, (team_id, _) in enumerate(sorted_teams, 1):
    if team_id == t:
        print (rank)
        break