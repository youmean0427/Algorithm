import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
cnt = {}
for _ in range(N):
    S = input().rstrip()
    if S in cnt:
        cnt[S] += 1
    else:
        cnt[S] = 1

arr = list(cnt.items())
arr.sort(key = lambda x : (-x[1], x[0]))
print(arr[0][0])