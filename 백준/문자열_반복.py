n = int(input())

for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    b = list(b)
    for i in range(len(b)):
        print(b[i] * a, end = '')
    print()