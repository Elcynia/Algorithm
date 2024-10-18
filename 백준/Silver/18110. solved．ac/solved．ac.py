import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = [int(input().strip()) for _ in range(n)]

if n == 0:
    print(0)
else:
    cut = int((n * 0.15) + 0.5)
    # print (cut)
    arr.sort()
    if cut > 0:
      arr2 = arr[cut:-cut]
    else:
      arr2 = arr
    
    if arr2:
        avg = sum(arr2) / len(arr2)
        difficulty = int(avg + 0.5)
    else:
        difficulty = 0
    
    print(difficulty)