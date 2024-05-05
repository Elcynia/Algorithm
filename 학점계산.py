import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
score = input()
if score == "A+":
  res = 4.3
elif score == "A0":
  res = 4.0
elif score == "A-":
  res = 3.7
elif score == "B+":
  res = 3.3
elif score == "B0":
  res = 3.0
elif score == "B-":
  res = 2.7
elif score == "C+":
  res = 2.3
elif score == "C0":
  res = 2.0
elif score == "C-":
  res = 1.7
elif score == "D+":
  res = 1.3
elif score == "D0":
  res = 1.0
elif score == "D-":
  res = 0.7
else:
  res = 0.0

print(res)