import sys,math
# sys.stdin = open('./input.txt', 'rt')
A,B,V = map(int, input().split())
days = math.ceil((V - A) / (A - B))
print (days+1)