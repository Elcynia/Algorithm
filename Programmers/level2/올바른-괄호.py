s = ")()("

def solution(s):
    cnt = 0
    answer = 0
    for i in list(s):
        if (i == '('):
            cnt += 1
        elif (i == ')'):
            cnt -= 1
            if (cnt < 0):
                print(False)
                return False
    if (cnt == 0):
        print(True)
        return True
    else:
        print(False)
        return False
solution(s)