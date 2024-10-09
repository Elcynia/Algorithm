import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
S = list(input().strip())
T = list(input().strip())

def AB(S, T):
    if S == T:
        return True
    if len(T) <= len(S):
        return False

    # 끝이 'A'인 경우
    if T[-1] == 'A':
        if AB(S, T[:-1]):
            return True

    # 시작이 'B'인 경우
    if T[0] == 'B':
        if AB(S, T[1:][::-1]):
            return True

    return False


print(1 if AB(S, T) else 0)