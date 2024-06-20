import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
stack = []
for i in input().strip():
    if i == "문제":
        stack.append("문제")
    elif i == "고무오리":
        if stack:
            stack.pop()
        else:
            stack.append("문제")
            stack.append("문제")
    elif i == "고무오리 디버깅 끝":
        break

if not stack:
    print("고무오리야 사랑해")
else:
    print("힝구")