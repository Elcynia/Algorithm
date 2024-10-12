import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
A, B = map(int, input().strip().split())
elements1 = set(map(int, input().strip().split()))
elements2 = set(map(int, input().strip().split()))
print (len(elements1-elements2) + len(elements2-elements1))