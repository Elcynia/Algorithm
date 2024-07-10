import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
for i in range(3):
  play = list(map(int, input().split()))
  배 = 0
  등 = 0
  for j in play:
    if (j == 0):
      배 += 1
    else:
      등 += 1
  if (배 == 1 and 등 == 3):
    print ('A')
  elif (배 == 2 and 등 == 2):
    print ('B')
  elif (배 == 3 and 등 == 1):
    print ('C')
  elif (배 == 4):
    print ('D')
  else:
    print ('E')