import sys
sys.stdin = open('./input.txt', 'rt')

if __name__ == "__main__":
  nums = [int(input()) for _ in range(10)]
  arr = []
  for i in nums:
    arr.append(i % 42)
  print (len(set(arr)))