import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
word = 'MOBIS'
n = input()

for i in word:
  if (i in n):
    n = n.replace(i, '', 1)
    print (n)
  else:
    print('NO')
    break
else:
  print('YES')
  

