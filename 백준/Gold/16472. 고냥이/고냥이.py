import sys

input = sys.stdin.readline

N = int(input())
arr = list(input().rstrip())
now = [arr[0]]
cnt = {}

i, j = 0, 0
answer = 0
t = 0

while i < len(arr):

    if arr[i] in cnt:
        cnt[arr[i]] += 1
    else:
        cnt[arr[i]] = 1
        t += 1

    if t > N:
        while t > N:
            cnt[arr[j]] -= 1
            if cnt[arr[j]] == 0:
                del cnt[arr[j]]
                t -= 1
            j += 1

    answer = max(answer, i - j + 1)
    i += 1

print(answer)