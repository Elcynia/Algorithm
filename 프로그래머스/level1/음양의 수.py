def solution(absolutes, signs):
    answer = 0
    for idx,i in enumerate(absolutes):
        if (signs[idx] == False):
            i=-i
        answer += i
    return answer
print(solution([4,7,12], [True, False, True]))