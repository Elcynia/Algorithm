import heapq, sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())

heap = []

for i in map(int, input().split()):
    heapq.heappush(heap, i)

for _ in range(N - 1):
    for i in map(int, input().split()):
        if i > heap[0]:
            heapq.heappush(heap, i)
            heapq.heappop(heap)

print(heap[0]) 