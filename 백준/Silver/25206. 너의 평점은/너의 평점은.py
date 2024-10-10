import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
sum_score = 0
sum_grade = 0
major_score = 0
for i in range(20):
  subject, score, grade = map(str, input().strip().split())
  if grade == 'P':
    continue
  sum_score += float(score)
  
  if grade == 'A+':
    sum_grade += 4.5
    major_score += 4.5 * float(score)
  elif grade == 'A0':
    sum_grade += 4.0
    major_score += 4.0 * float(score)
  elif grade == 'B+':
    sum_grade += 3.5
    major_score += 3.5 * float(score)
  elif grade == 'B0':
    sum_grade += 3.0
    major_score += 3.0 * float(score)
  elif grade == 'C+':
    sum_grade += 2.5
    major_score += 2.5 * float(score)
  elif grade == 'C0':
    sum_grade += 2.0
    major_score += 2.0 * float(score)
  elif grade == 'D+':
    sum_grade += 1.5
    major_score += 1.5 * float(score)
  elif grade == 'D0':
    sum_grade += 1.0
    major_score += 1.0 * float(score)
  elif grade == 'F':
    sum_grade += 0
    major_score += 0 * float(score)
    
print ('0.000000' if sum_score == 0 else f"{major_score / sum_score:.6f}")
