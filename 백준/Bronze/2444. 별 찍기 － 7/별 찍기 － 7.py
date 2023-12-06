import sys
input = sys.stdin.readline

N = int(input())

i = 1
minus = 2
cnt = 1
while cnt <= 2*N-1:
    print(" " * (N-i), end="")
    print("*" * (2*i-1), end="")
    print(" ")

    if cnt >= N:
        i = cnt+1 - minus
        minus += 2
    else:
        i += 1

    cnt += 1