import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
people, award = map(int, input().split())
students = sorted(list(map(int, input().split())))
print (students[-award])
