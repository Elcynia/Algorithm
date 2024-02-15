import sys
# sys.stdin = open('./input.txt', 'rt')
if __name__ == "__main__":
  arr = list(map(int, input().split()))
  ascending, descending = True, True
  for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        descending = False
    elif arr[i] < arr[i - 1]:
        ascending = False

  if ascending:
      print("ascending")
  elif descending:
      print("descending")
  else:
      print("mixed")
