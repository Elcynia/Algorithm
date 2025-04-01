import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    person = 0
    for i in range(k):
        person = person * 2 + 1
    
    print(person)


