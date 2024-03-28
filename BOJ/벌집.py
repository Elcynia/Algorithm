# import sys
# sys.stdin = open('./input.txt', 'rt')
n = int(input())

if n == 1: # 1은 방 개수가 하나인 것이 자명하므로 고정
    print(1)
else:
    total_room = 1 # 전체 방 개수
    honeycomb = 6 # 주변 한 바퀴 돌면 나오는 개수
    room_cnt = 1  # 방 주변 개수 카운트용
    while 1:
      room_cnt += honeycomb
      total_room += 1
      honeycomb += 6
      if n <= room_cnt:
        print(total_room)
        break