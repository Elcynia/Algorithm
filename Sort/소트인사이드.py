import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n  = sorted(list(input()), reverse=True)
print ("".join(n))