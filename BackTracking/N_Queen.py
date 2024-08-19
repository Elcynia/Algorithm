import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
cnt = 0
isused1 = [False] * 40 # column
isused2 = [False] * 40 # row
isused3 = [False] * 40

def func(cur):
  global cnt, n
  if cur == n:
    cnt += 1
    return
  for i in range(n):
    if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1]:
      continue
    isused1[i] = True
    isused2[i + cur] = True
    isused3[cur - i + n - 1] = True
    func(cur + 1)
    isused1[i] = False
    isused2[i + cur] = False
    isused3[cur - i + n - 1] = False

func(0)
print(cnt)
