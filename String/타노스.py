import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

n = input().strip()
arr1 = []
arr2 = []

for i in n:
    if i == '1':
        arr1.append(i)
    else:
        arr2.append(i)

a = len(arr1) // 2
b = len(arr2) // 2

cal = []
zero_cnt = 0
one_cnt = 0

for char in n:
    if char == '0':
        if zero_cnt < b:
            cal.append(char)
            zero_cnt += 1
    else:
        if one_cnt < a:
            one_cnt += 1
        else:
            cal.append(char)

print(''.join(cal))