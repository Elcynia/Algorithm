def solution(s):
    cnt = 0 
    cnt2 = 0
    while s != '1':
        filtering = len(s.replace('0', ''))
        cnt += 1
        cnt2 += len(s) - filtering
        s = bin(filtering)[2:]
    return [cnt, cnt2]

print (solution("110010101001"))