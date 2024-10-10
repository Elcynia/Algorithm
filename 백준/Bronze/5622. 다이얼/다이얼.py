import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
dials = {
  '': 1,
  'ABC': 2,
  'DEF': 3,
  'GHI': 4,
  'JKL': 5,
  'MNO': 6,
  'PQRS': 7,
  'TUV': 8,
  'WXYZ': 9,
  'OPERATOR': 0,
}
word = list(input().strip())
r = []
for i in range(len(word)):
  for key, value in dials.items():
    if word[i] in key:
      r.append (value)
      break
      
total_time = sum(value + 1 for value in r)
print(total_time)