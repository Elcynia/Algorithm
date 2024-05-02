s = "3people unFollowed me"	
def solution(s):
    answer = []
    s = s.split(' ')
    for i in range(len(s)):
       s[i] = s[i][0].upper() + s[i][1:].lower()
    # print(" ".join(s))
    return  " ".join(s)



solution(s)
