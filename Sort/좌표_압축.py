import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())
coords = list(map(int, input().split()))
# 좌표 압축 (정렬 및 중복 제거)
sorted_coords = sorted(set(coords))

# 각 좌표가 정렬된 리스트에서 어디에 위치하는지 인덱스를 저장
coord_idx = {coord: idx for idx, coord in enumerate(sorted_coords)}

# 원래 좌표 리스트를 순회하면서 압축된 인덱스를 출력
compressed_coords = [coord_idx[coord] for coord in coords]
print(' '.join(map(str, compressed_coords)))