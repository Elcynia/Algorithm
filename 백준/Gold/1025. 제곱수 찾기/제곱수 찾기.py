import math

def is_square(n):
  if n < 0:
    return False
  root = int(math.sqrt(n))
  return root * root == n

def find_largest_square_number():
  n, m = map(int, input().split())
  grid = [input().strip() for _ in range(n)]
  max_square = -1
  
  for i in range(n):
    for j in range(m):
      for di in range(-n, n + 1):
        for dj in range(-m, m + 1):
          if di == 0 and dj == 0:
            continue
          
          num = ""
          x, y = i, j
          while 0 <= x < n and 0 <= y < m:
            num += grid[x][y]
            try:
              num_int = int(num)
              if is_square(num_int):
                max_square = max(max_square, num_int)
            except ValueError:
              break  
            x += di
            y += dj
  
  return max_square

print(find_largest_square_number())
