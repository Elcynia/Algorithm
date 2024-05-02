A, B = [1,4,2], [5,4,4]

def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for a, b in zip(A, B):
        answer += a * b
    return answer

solution(A,B)
    # for i in range(len(A)):
    #     answer += A[i]*B[i]
    #     print (answer)