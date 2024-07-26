import sys
sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline
nums = list(map(int, input().split()))
nums.sort()
print (nums[0], nums[1], nums[2])