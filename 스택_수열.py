import sys
# sys.stdin = open('./input.txt', 'r')
n = int(sys.stdin.readline())
stack = []     
res = []      

count = 1
valid = True

for _ in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        res.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        valid = False
        break
if valid:
    print('\n'.join(res))
else:
    print('NO')