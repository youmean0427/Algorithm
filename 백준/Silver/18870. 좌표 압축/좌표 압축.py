import sys
input = sys.stdin.readline

N = int(input())
arr = [int(x) for x in input().split()]

cnt = {}
check = list(set(arr))
check.sort()
result = []

for i in range(len(check)):
    cnt[check[i]] = i

for k in arr:
    print(cnt[k], end =' ')