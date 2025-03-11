import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().strip().split(' ')))
mx = sum(S)
possible_sums = set()

def generate_sums(idx, subset_sum):
    if idx == N:
        possible_sums.add(subset_sum)
        return
    
    generate_sums(idx + 1, subset_sum + S[idx])
    generate_sums(idx + 1, subset_sum)

generate_sums(0, 0)

for i in range(1, mx + 2):
    if i not in possible_sums:
        print(i)
        break
