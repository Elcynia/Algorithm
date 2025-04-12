import sys
input = sys.stdin.readline
N, A, B = map(int, input().strip().split())
subway_time = max(N, B)

if A < subway_time:
    print("Bus")
elif A > subway_time:
    print("Subway")
else:
    print("Anything")