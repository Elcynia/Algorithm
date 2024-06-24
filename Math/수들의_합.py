'''
이차방정식, 근의 공식
'''

import sys, math
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
s = int(input())

def find_max_n(s):
    # 이차방정식의 계수
    a = 1
    b = 1
    c = -2 * s
    
    # 근의 공식
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # 실근 존재 X
    
    n = (-b + math.sqrt(discriminant)) / (2 * a)
    max_n = int(n)
    
    # max_n개의 자연수 합이 s와 같거나 작은지 판별
    if (max_n * (max_n + 1)) // 2 <= s:
        return max_n
    else:
        return max_n - 1
      
# print(find_max_n(s))

''' simple ver '''
n = 0
while n * (n + 1) / 2 <= s:
  n += 1
print (n-1)