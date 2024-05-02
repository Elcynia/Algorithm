def solution(n):
    answer = []
    for _ in range(len(str(n))):
        answer.append(n % 10)  # 맨 앞에 현재 자릿수의 값을 그대로 추가합니다.
        n //= 10
    print(answer)
    return answer

solution(12345)
