def Harshad(n):
  print (int(x) for x in str(n))
    # return n % sum(int(x) for x in str(n)) == 0

def solution(x):
    tmp = x
    sum = 0
    for _ in str(x):
      sum += x % 10
      x //= 10
    if (tmp % sum == 0 ):
       return True
    else:
       return False

print(Harshad(13))