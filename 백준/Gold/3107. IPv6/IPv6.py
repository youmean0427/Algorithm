import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

S = input().rstrip()
arr = S.split(":")
check = 0

if len(arr) >= 8:
    check = 1

if len(arr) < 8:
    for k in range(len(arr)):
        if arr[k] == '':
            arr = arr[:k+1] + [''] * (8 - len(arr)) + arr[k+1:]

if check == 1:
    if arr[-1] == "":
        arr = arr[:8]
    elif arr[0] == "":
        arr = arr[1:]

for i in range(len(arr)):
    x = 4 - len(arr[i])
    arr[i] = ("0" * x) + arr[i][::]

print(":".join(arr))
