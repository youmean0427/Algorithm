import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    total = 0
    for i in range(1, n):
        for j in range(i+1, n):

            cnt = ((i ** 2) + (j ** 2) + m) / (i * j)
            if cnt.is_integer():
                total += 1

    print(total)