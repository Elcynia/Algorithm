import sys
from collections import deque
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

left = deque(input().strip())
right = deque()
N = int(input())

for _ in range(N):
    command = input().strip().split()
    if command[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.popleft())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(''.join(left + right))