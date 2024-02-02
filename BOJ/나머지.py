 
def solution(A,B,C):
  answer = []
  answer.append((A+B)%C)
  answer.append(((A%C) + (B%C))%C)
  answer.append((A*B)%C)
  answer.append(((A%C) * (B%C))%C)
  for i in answer:
    print (i)


if __name__ == "__main__":
  a, b, c = map(int, input().split(' '))
  solution(a,b,c)