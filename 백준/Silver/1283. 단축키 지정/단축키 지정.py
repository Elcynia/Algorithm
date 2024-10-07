import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
shortkeys = set()
keys = []

for _ in range(n):
  cmd = input().strip().split()
  found = False
  # 1. 첫 글자 확인
  for idx, word in enumerate(cmd):
    if not word[0].upper() in shortkeys:
      shortkeys.add(word[0].upper()) # 첫 글자 대문자
      cmd[idx] = f"[{word[0]}]{word[1:]}" # [N]ew
      found = True
      break
  
  # 첫번째 조건 불일치 시, 왼쪽부터 차례대로 확인
  if not found:
    for idx, word in enumerate(cmd):
      for j, char in enumerate(word):
        if not char.upper() in shortkeys:
          shortkeys.add(char.upper())
          cmd[idx] = f"{word[:j]}[{char}]{word[j+1:]}"
          found = True
          break
      if found:
        break
  
  keys.append(' '.join(cmd))

for i in keys:
  print(i)