import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
r = ''
for i in sys.stdin.readlines():
	r += i.replace('\n','')
print(sum(map(int, r.split(','))))