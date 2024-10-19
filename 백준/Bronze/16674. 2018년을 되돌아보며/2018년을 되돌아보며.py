import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = input().strip()
count = {
  '2': 0,
  '0': 0,
  '1': 0,
  '8': 0
}

for digit in N:
  if digit in count:
    count[digit] += 1

# 숫자 외 다른 숫자가 포함되어 있는 경우
if len(N) != sum(count.values()):
  print(0)
# 2018에 해당하는 숫자가 하나도 없는 경우
elif all(v == 0 for v in count.values()):
  print(0)
# 2018이 정확히 균일하게 분포된 경우
elif count['2'] == count['0'] == count['1'] == count['8']:
  print(8)
# 2018 숫자가 적어도 하나씩 존재하지만 균일하지 않은 경우
elif all(v > 0 for v in count.values()):
  print(2)
else:
  print(1)