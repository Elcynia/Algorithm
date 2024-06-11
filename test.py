def diamond(height):
    if height % 2 == 0:  # 높이가 짝수면 홀수로 변경
        height += 1
    
    mid = height // 2 + 1
    for i in range(1, mid + 1):
        print(' ' * (mid - i) + '*' * (2 * i - 1))
    for i in range(mid - 1, 0, -1):
        print(' ' * (mid - i) + '*' * (2 * i - 1))

# 사용 예시
diamond(30)
