import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
exp = input().strip()
S = []
res = ''

for i in exp:
  if i.isalpha():
    res += i
  elif i == '(':
        S.append(i)
  elif i == ')':
    while S and S[-1] != '(':
      res += S.pop()
    if S and S[-1] == '(':
          S.pop()  # '(' 제거
  elif i in ('*', '/'):
    while S and S[-1] in ('*', '/'):
      res += S.pop()
    S.append(i)
  elif i in ('+', '-'):
    while S and S[-1] != '(':
      res += S.pop()
    S.append(i)

# 스택에 남아있는 연산자 처리
while S:
    res += S.pop()

print(res)