import sys
# sys.stdin = open('./input.txt', 'rt')
if __name__ == "__main__":
  n = int(input())
  arr = list(map(float, input().split()))
  new = [score / max(arr) * 100 for score in arr]
  average = sum(new) / n
  print("%.2f"%average)
  
