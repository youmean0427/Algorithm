import sys

input=sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
cnt = {}

for i in arr1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

# print(cnt)

for k in arr2:
    if k in cnt:
        print(cnt[k], end=' ')
    else:
        print(0, end=' ')
