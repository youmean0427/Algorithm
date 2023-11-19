import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = [{} for _ in range(M)]

for _ in range(N):
    x = (input().rstrip())

    for i in range(M):
        if x[i] in arr[i]:
            arr[i][x[i]] += 1
        else:
            arr[i][x[i]] = 1

answer = []
cnt = 0
for k in range(M):
    x = sorted(arr[k].items(), key=lambda x: (-x[1],x[0]))
    answer.append(x[0][0])

    for j in range(1, len(x)):
        cnt += x[j][1]


print("".join(answer))
print(cnt)