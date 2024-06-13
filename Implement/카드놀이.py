import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score, b_score = [], []
for i in range(10):
    if a[i] == b[i]:
        a_score.append(1)
        b_score.append(1)
    elif a[i] > b[i]:
        a_score.append(3)
        b_score.append(0)
    else:
        b_score.append(3)
        a_score.append(0)

print(sum(a_score), sum(b_score))

def drawCal():
    for i in range(10):
        if a_score[9 - i] > b_score[9 - i]:
            print('A')
            return
        elif a_score[9 - i] < b_score[9 - i]:
            print('B')
            return
    print('D')

if sum(a_score) == sum(b_score):
    drawCal()
elif sum(a_score) > sum(b_score):
    print('A')
else:
    print('B')
