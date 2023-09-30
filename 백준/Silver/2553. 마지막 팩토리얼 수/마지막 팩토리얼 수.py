import sys
input = sys.stdin.readline
from math import factorial

N = int(input())
num = str(factorial(N))

for i in num[::-1]:
    if i == '0':
        pass
    else:
        print(i)
        break