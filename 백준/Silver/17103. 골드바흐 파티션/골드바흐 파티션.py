import sys, math
input = sys.stdin.readline


def prime_list(n):
    arr = [True] * (n+1)

    for i in range(2, n+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = False

    return arr

T = int(input())
prime = prime_list(1000000)
prime[0], prime[1] = False, False

for _ in range(T):
    x = int(input())
    cnt = 0
    for i in range(2, x):
        if prime[i] and prime[x-i]:
            cnt += 1

    print(math.ceil(cnt/2))

