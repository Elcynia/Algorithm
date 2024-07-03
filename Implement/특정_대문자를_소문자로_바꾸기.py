import sys
#sys.stdin = open('./input.txt', 'r')
a = list(input())
c = input().split()
ans = []
for i in range(len(a)):
  for j in range(len(c)):
    if (a[i] == c[j]):
      a[i] = a[i].lower()

print (''.join(a))