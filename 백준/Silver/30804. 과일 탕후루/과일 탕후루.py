import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
start = 0
end = 0

def fruit(x, y):
    cnt = 0
    for i in visited:
        if i:
            cnt += 1
    if (cnt >= 3):
        return 0
    return 1

ans = 0
visited = [0 for _ in range(10)]
visited[arr[0]] = 1
while (end < n):

    if (fruit(start, end)):
        ans = max(ans, end - start + 1)
        end += 1
        if (end < n):
            visited[arr[end]] += 1
    else:
        visited[arr[start]] -= 1
        start += 1

print(ans)