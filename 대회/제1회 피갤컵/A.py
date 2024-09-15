import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
N = int(input())
arr = input()
def process_string(s):
    while "PS4" in s or "PS5" in s:
        new_s = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i:i+2] == "PS" and s[i+2] in ["4", "5"]:
                new_s += "PS"
                i += 3
            else:
                new_s += s[i]
                i += 1
        s = new_s
    return s

print (process_string(arr))