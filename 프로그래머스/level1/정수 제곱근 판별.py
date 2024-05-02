def solution(n):
    answer = 0;
    if ((n**0.5) %1 == 0): return ((n**0.5)+1)**2
    else: return -1


print(solution(121))
