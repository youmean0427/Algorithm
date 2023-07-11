import sys

M, N = map(int, sys.stdin.readline().split())

def isPrime(x):
    if x == 1:
        return False
    else:
        for k in range(2, int(x ** 0.5)+1):
            if x % k == 0:
                return False

        return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)
