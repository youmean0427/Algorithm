import sys
input = sys.stdin.readline

N = int(input())
arr = {}
for _ in range(N):
    a, b = input().split()

    if b == "enter":
        arr[a] = 1
    elif b == 'leave':
        arr[a] = 0

arr = sorted(arr.items(), reverse=True)
for i in arr:
    if i[1] == 1:
        print(i[0])