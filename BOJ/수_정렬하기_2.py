import sys
sys.stdin = open('./input.txt', 'rt')

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

sorted_arr = sorted(arr)

for i in sorted_arr:
    print(i)