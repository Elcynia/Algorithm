import sys
sys.stdin = open('input.txt', 'r')

def 재귀(x):
  if x == 0:
    return
  else:
    재귀(x//2)
    print (x % 2, end='')


if __name__ == "__main__":
  n = int(input())
  재귀(n)
