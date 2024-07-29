import sys
#sys.stdin = open('./input.txt', 'r')
arr = input()
for i in range(0, len(arr), 10):
  print (arr[i:i+10])
