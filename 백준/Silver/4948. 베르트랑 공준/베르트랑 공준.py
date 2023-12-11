import sys, math
input = sys.stdin.readline


def prime_list(start, n):

    arr = [True] * (n+1)
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if arr[i] == True:
            for j in range(2*i, n+1, i):
                arr[j] = False

    arr = [i for i in (arr[start+1:n+1]) if i == True]

    return len(arr)

while True:
    x = int(input())

    if x == 0:
        exit(0)

    print(prime_list(x,2*x))