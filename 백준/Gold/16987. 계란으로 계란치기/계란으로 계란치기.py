import sys

# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append(([a, b]))

# a : 내구도, b : 무게

ans = 0


def dfs(n, cnt):
    global ans

    # 가지치기
    # 남은 횟수를 모두 진행해도, ans보다 작거나 같을 경우
    if ans >= (cnt + (N-n) * 2):
        return

    if n == N:
        ans = max(ans, cnt)
        return


    if arr[n][0] <= 0:  # 현재 계란이 깨진 경우, 다음 계란
        dfs(n + 1, cnt)
    else:  # 현재 계란이 깨지지 않은 경우, 계란치기

        flag = False  # 한번도 안 부딪힌 경우, 다음 계란
        for i in range(N):

            if n == i or arr[i][0] <= 0:
                continue
            flag = True
            arr[n][0] -= arr[i][1]
            arr[i][0] -= arr[n][1]
            dfs(n + 1, cnt + int(arr[n][0] <= 0) + int(arr[i][0] <= 0))
            arr[n][0] += arr[i][1]
            arr[i][0] += arr[n][1]

        if flag == False:
            dfs(n + 1, cnt)


dfs(0, 0)
print(ans)
