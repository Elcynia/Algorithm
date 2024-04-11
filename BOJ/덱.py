import sys
sys.stdin = open('./input.txt', 'r')
n = int(sys.stdin.readline())

dquque = []
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        dquque.insert(0, int(command[1]))
    elif command[0] == 'push_back':
        dquque.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(dquque) == 0:
            print(-1)
        else:
            print(dquque.pop(0))
    elif command[0] == 'pop_back':
        if len(dquque) == 0:
            print(-1)
        else:
            print(dquque.pop())
    elif command[0] == 'size':
        print(len(dquque))
    elif command[0] == 'empty':
        if len(dquque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dquque) == 0:
            print(-1)
        else:
            print(dquque[0])
    elif command[0] == 'back':
        if len(dquque) == 0:
            print(-1)
        else:
            print(dquque[-1])