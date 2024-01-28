import sys
sys.stdin = open('./input.txt', 'r')


if __name__ == "__main__":
  n = input()
  score = sorted(list(map(float, input().split(' '))), reverse=True)
  # print (score[1]/score[0]*100)
  # print (score)
  print (1/100*100)
