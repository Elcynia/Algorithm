import sys
# sys.stdin = open('./input.txt', 'rt')
if __name__ == "__main__":
  n = int(input())
  for _ in range(n):
    h, w, customer = map(int, input().split())
    floor = customer % h # 10(번째 손님) % 6(최고 층 높이) = 4 (사용할 층)
    room = customer // h+1 # 10 // 6 + 1 = 2(방 호수)
    if floor == 0: # 배정될 층수가 최대 높이 층수에 도달했을 때 (나머지가 0이 될 때)
      floor = h # 층을 h로 바꾸고
      room -= 1 # 방의 호수를 하나 감소시킨다 (다시 **1호로 시작하기 위함)
    print("%d%02d" % (floor, room))
