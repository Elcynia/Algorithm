import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
arr = [input().strip() for _ in range(3)]

# 마지막 숫자 찾기
for i in range(2, -1, -1):
    if arr[i].isdigit():
        ans = int(arr[i]) + (3-i)
        break

if ans % 15 == 0: # 3 or 5의 배수 체크
    print('FizzBuzz')
elif ans % 3 == 0: # only 3
    print('Fizz')
elif ans % 5 == 0: # only 5
    print('Buzz')
else:
    print(ans)