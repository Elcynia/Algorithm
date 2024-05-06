import sys, re
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

def valid(word):
    if not re.search('[aeiou]', word):
        return False
    if re.search('[aeiou]{3}|[^aeiou]{3}', word):
        return False
    # 같은 글자가 연속적으로 두번 오는지 확인
    if re.search('(.)\\1', word) and not re.search('(ee)|(oo)', word):
        return False
    return True

while True:
    word = input().strip()
    if word == 'end':
        break
    if valid(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")