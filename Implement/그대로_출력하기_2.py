import sys
sys.stdin = open('./input.txt', 'r')

while True:
    try:
        print(input())
    except EOFError:
        break