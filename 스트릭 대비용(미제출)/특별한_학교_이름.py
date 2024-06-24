import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

s = input().strip()
if (s == 'NLCS'): 
  print ("North London Collegiate School")
elif (s == 'BHA'):
  print ("Branksome Hall Asia")
elif (s == 'KIS'):
  print ("Korea International School")
elif (s == 'SJA'):
  print ("St. Johnsbury Academy")
  