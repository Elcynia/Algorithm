# import sys
# sys.stdin = open('./input.txt', 'rt')
  
def valid(arr):
    stack = []
    for char in arr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0
def solve():
    n = int(input())  
    for _ in range(n):
        arr = str(input())
        if valid(arr):
            print("YES")
        else:
            print("NO")

solve()
