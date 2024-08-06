import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
nums = list(map(int, input().split()))
cal1 = abs(nums[0]-nums[1]) + 1
print (cal1 * (nums[0] + nums[1]) // 2)