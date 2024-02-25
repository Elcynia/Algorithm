import sys
# sys.stdin = open('./input.txt', 'rt')
if __name__ == "__main__":
  sugar = int(input())
  box  = 0
  while sugar >= 0 :
      if sugar % 5 == 0 : 
          box += (sugar // 5) 
          print(box)
          break
      sugar -= 3  
      box += 1  
  else :
      print(-1)
  