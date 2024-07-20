import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
entered = set()

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        entered.add(name)
    else:
        entered.remove(name)

print ('\n'.join(sorted(entered, reverse=True)))