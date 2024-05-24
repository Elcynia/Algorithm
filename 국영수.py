import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())
students = []
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append([name, int(kor), int(eng), int(math)])

students.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

for student in students:
    print(student[0])