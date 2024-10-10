import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
word = input().strip()
for char in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
  word = word.replace(char, 'A')
print(len(word))