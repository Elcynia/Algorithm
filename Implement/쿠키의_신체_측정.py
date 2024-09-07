import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
body = [[''] + list(input().rstrip()) for _ in range(n)]
body.insert(0, [''] * (n+1))
heart = []
left_arms = 0
right_arms = 0
back = 0
left_legs = 0
right_legs = 0

# 심장 수집
for i in range(1, n+1):
  for j in range(1, n+1):
    if (body[i][j] == '*'):
      heart = [i+1, j]
      break
  if heart:
    break
    
# 나머지 신체 조각 수집

# 왼팔
left_arms_piece = heart[1] - 1
while left_arms_piece > 0 and body[heart[0]][left_arms_piece] == '*':
    left_arms += 1
    left_arms_piece -= 1
    

# 오른팔
right_arms_piece = heart[1] + 1
while right_arms_piece <= n and body[heart[0]][right_arms_piece] == '*':
  right_arms += 1
  right_arms_piece += 1

# 등
back_piece = heart[0] + 1
while back_piece <= n and body[back_piece][heart[1]] == '*':
    back += 1
    back_piece += 1

waist_end = heart[0] + back

# 왼쪽 다리 길이 측정
left_legs_piece = waist_end + 1
while left_legs_piece <= n and body[left_legs_piece][heart[1]-1] == '*':
    left_legs += 1
    left_legs_piece += 1

# 오른쪽 다리 길이 측정
right_legs_piece = waist_end + 1
while right_legs_piece <= n and body[right_legs_piece][heart[1]+1] == '*':
    right_legs += 1
    right_legs_piece += 1
    

print (*heart)
print (left_arms, right_arms, back, left_legs, right_legs)