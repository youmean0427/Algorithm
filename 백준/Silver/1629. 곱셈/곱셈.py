import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a, n):
    if n == 0:
        return 1
    else:
        x = power(a, n//2)
        if (n % 2 == 0):
            return (x * x) % C
        else:
            return (x * x * a) % C

print(power(A, B))