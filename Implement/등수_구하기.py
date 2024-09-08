import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
else:
  scores = list(map(int, input().split()))
  if N == P and new_score <= scores[-1]:
      print(-1)
  else:
    scores.append(new_score)
    scores.sort(reverse=True)
    rank = scores.index(new_score) + 1
    if rank <= P:
        print(rank)
    else:
        print(-1)