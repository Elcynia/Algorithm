import sys, math
#sys.stdin = open('./input.txt', 'r')
t = int(input())
for i in range(t):
  scores = list(map(float, input().split()))
  n = scores[0]
  students_scores = scores[1:]
  total_score = sum(students_scores)
    
  avg = total_score / n
  cnt_avg = sum(1 for i in students_scores if i > avg)
  ratio = (cnt_avg / n) * 100
  print(f"{ratio:.3f}%")