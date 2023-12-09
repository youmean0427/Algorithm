import sys
input = sys.stdin.readline

N = int(input())
result = []

def fin(N):
    for i in range(2, N+1):
        if N % i == 0:
            a = i
            result.append(a)
            break

    b = N // a
    if b > a:
        fin(b)
    elif b != 1:
        result.append(b)

if N != 1:
    fin(N)

    for i in result:
        print(i)