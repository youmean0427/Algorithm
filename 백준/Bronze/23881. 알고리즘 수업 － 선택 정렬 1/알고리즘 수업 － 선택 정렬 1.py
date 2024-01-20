import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(i) for i in input().split()]
num = []

def selection_sort(arr, N):
    global num
    cnt = 0
    for i in range(N-1, 0, -1):
        max_val = arr[N-1]
        max_idx = N-1
        for k in range(i):
            if arr[k] > max_val:
                max_val = arr[k]
                max_idx = k

        if arr[N-1] != arr[max_idx]:
            arr[N-1], arr[max_idx] = arr[max_idx], arr[N-1]
            cnt += 1

        if cnt == K:
            num = [arr[N-1], arr[max_idx]]

        N -= 1

    return cnt

x = selection_sort(arr, N)
if x >= K:
    num.sort()
    print(*num)
else:
    print(-1)