import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM (a, b):
    return a * b / GCD(a, b)

print(int(LCM(A, B)))