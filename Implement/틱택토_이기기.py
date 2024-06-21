import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.read

def check_winner(board, player):
    # 가로, 세로, 대각선 확인
    for i in range(3):
        # 가로 확인
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # 세로 확인
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def find_winning_move(board, player):
    # 가능한 모든 빈 칸에 대해 시도
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                # 빈 칸에 player 말을 놓고 이길 수 있는지 확인
                board[i][j] = player
                if check_winner(board, player):
                    return True, board
                # 다시 원래대로 돌려놓음
                board[i][j] = '-'
    return False, None

def print_board(board):
    for row in board:
        print(''.join(row))

data = input().strip().split('\n')
T = int(data[0].strip())

index = 1
for case in range(1, T + 1):
    print(f'Case {case}:')
    board = [list(data[index]), list(data[index + 1]), list(data[index + 2])]
    player = data[index + 3].strip()
    
    # 현재 플레이어가 'x'면 남규는 'o'를 놓아야 함
    if player == 'x':
        turn = 'o'
    else:
        turn = 'x'
    
    # 남규가 다음 한 수로 이길 수 있는 상태 찾기
    found, new_board = find_winning_move(board, turn)
    
    if found:
        print_board(new_board)
    else:
        # 예외 상황 처리: 주어진 조건에서는 이 경우가 발생하지 않아야 함
        print("Unexpected input condition: No winning move found")
    
    print()  # 테스트 케이스 사이에 빈 줄 출력
    index += 4  # 다음 테스트 케이스 준비
