import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
P, M = map(int, input().split())
rooms = []

for _ in range(P):
    level, player = input().split()
    level = int(level)
    
    joined = False
    for room in rooms:
        if len(room) < M and room[0][0] - 10 <= level <= room[0][0] + 10:
            room.append((level, player))
            joined = True
            break
    
    # 새 방
    if not joined:
        rooms.append([(level, player)])

for room in rooms:
    if len(room) == M:
        print("Started!")
    else:
        print("Waiting!")
    
    for level, player in sorted(room, key=lambda x: x[1]):
        print(level, player)
