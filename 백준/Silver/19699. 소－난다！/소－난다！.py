import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(i) for i in input().split()]
ans = set()


def prime(num):
    for i in range(2, int(num ** (1/2))+1):
        if num % i == 0:
            return False
    return True


def dfs(n, sm):
    global ans
    if len(sm) == M:
        total = sum(sm)
        if prime(total):
            ans.add(total)
        return

    if n >= len(arr):
        return

    dfs(n+1, sm+[arr[n]])
    dfs(n+1, sm)


dfs(0, [])
if len(ans) == 0:
    print(-1)
else:
    answer = list(ans)
    answer.sort()
    print(*answer)
