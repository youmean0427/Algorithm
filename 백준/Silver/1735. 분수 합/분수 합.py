import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return a * b / GCD(a, b)

m = int(LCM(b, d))
n = int(a * (m / b) + c * (m / d))

k = GCD(n, m)
print(n // k, m // k )