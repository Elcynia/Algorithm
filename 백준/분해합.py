import sys
def LoadInput():
  sys.stdin = open('./input.txt', 'r') if sys.stdin.isatty() else open('/dev/stdin', 'r')
if __name__ == "__main__":
  LoadInput()
  n = int(sys.stdin.readline()) 
  for i in range(n):
      digits = 0
      for j in str(i):
        digits += int(j)
      if (i + digits == n):
         print (i)
         break
  else:
     print (0)
      