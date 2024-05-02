import sys
# sys.stdin = open('./input.txt', 'rt')

if __name__ == "__main__":
  n = list(map(str, input().lower()))
  cnt = [0]*26
  for i in n:
    if ('a' <= i <= 'z'):
      cnt[ord(i) - ord('a')] += 1
  if (cnt.count(max(cnt))) > 1:
    print ("?")
  else:
    print(chr(cnt.index(max(cnt)) + ord('a')).upper())