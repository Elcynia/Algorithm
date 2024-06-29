import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
patient = input()
doctor = input()
if (len(doctor) > len(patient)): 
  print ('no')
else:
  print ('go')