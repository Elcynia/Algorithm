import sys
# sys.stdin = open('./input.txt', 'rt')
n = int(input())
arr = []
for _ in range(n):
  word = str(input())
  arr.append(word)
sorted_arr = sorted(set(arr), key=lambda x : (len(x), x))
print("\n".join(sorted_arr))