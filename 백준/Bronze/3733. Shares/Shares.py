while True:
    try:
        N, S = map(int, input().strip().split())
        print ((S // (N + 1)))
    except EOFError:
        break;