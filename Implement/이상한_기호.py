#연산자의 기호는 ＠으로, A＠B = (A+B)×(A-B)으로 정의내리기로 했다.
import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())
print((a+b) * (a-b))
