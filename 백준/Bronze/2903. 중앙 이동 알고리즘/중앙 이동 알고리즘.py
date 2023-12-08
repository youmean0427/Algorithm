import sys
input = sys.stdin.readline

arr = [4, 9, 25, 81]
N = int(input())

cnt = 8
i = 4
while i <= N:
    x = int(arr[i-1] ** (1/2))
    arr.append((x + cnt) ** 2)
    cnt *= 2
    i += 1

print(arr[N])