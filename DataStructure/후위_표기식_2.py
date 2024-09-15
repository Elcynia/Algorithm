import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
expression = input().rstrip()
nums=[int(input().rstrip()) for _ in range(n)]
S = []

for i in expression:
    if 'A' <= i <= 'Z':
        S.append(nums[ord(i)-ord('A')])
    else:
      b = S.pop()
      a = S.pop()
      if i == '+':
        S.append(a + b)
      elif i == '-':
        S.append(a - b)
      elif i == '*':
        S.append(a * b)
      elif i == '/':
        S.append(a / b)
      
print("{:.2f}".format(*S))