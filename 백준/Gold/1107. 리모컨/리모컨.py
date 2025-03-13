import sys
input = sys.stdin.readline

# 입력 부분 수정
N = int(input().strip())  # 이동하려고 하는 채널(정수로 변환)
M = int(input().strip())  # 고장난 버튼의 개수
broken = []
if M > 0:  # 고장난 버튼이 있는 경우에만 입력 받기
    broken = list(map(int, input().strip().split()))  # 고장난 버튼


# 특정 채널로 이동 가능한지 확인하는 함수
def can_press(channel):
    # 채널이 0인 경우 특별 처리
    if channel == 0:
        return 0 not in broken
    
    # 각 자릿수 확인
    digits = 0
    while channel > 0:
        if channel % 10 in broken:  # 해당 자릿수가 고장난 버튼인지 확인
            return False
        channel //= 10
        digits += 1
    return digits  # 버튼 누른 횟수 반환

def min_clicks():
    # 현재 채널(100)에서 +/- 버튼만 사용하는 경우
    min_count = abs(N - 100)
    for channel in range(1000001):
        digits = can_press(channel)
        if digits:  # 해당 채널로 직접 이동 가능하면
            # 숫자 버튼 누른 횟수 + +/- 버튼 누른 횟수
            count = digits + abs(channel - N)
            min_count = min(min_count, count)
    
    return min_count

print(min_clicks())