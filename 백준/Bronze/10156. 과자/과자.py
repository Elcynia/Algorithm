k, n, m = map(int, input().strip().split())
if (k*n < m):
    print (0)
else:
    print (k*n - m)
