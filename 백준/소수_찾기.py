import sys
sys.stdin = open('./input.txt', 'rt')

def is_prime(num):
    if num < 2: # 2보다 작으면 소수 아님
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    ans = 0
    numbers = list(map(int, input().split()))

    for num in numbers:
        if is_prime(num):
            ans += 1

    print(ans)
