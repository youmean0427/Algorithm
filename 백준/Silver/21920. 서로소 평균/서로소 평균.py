import sys
input = sys.stdin.readline

M = int(input())
arr = [int(x) for x in input().split()]
X = int(input())

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

sum_result = 0
cnt_result = 0
for i in arr:
    if GCD(i, X) == 1:
        sum_result += i
        cnt_result += 1


print((sum_result/cnt_result))


