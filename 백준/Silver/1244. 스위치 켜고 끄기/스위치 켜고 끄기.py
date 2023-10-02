import sys
input = sys.stdin.readline


C = int(input())
arr = [int(x) for x in input().split()]
K = int(input())

for _ in range(K):
    s, n = map(int, input().split())

    if s == 1: #남학생
        pass
        for i in range(n-1, C, n):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1

    else: # 여학생
        start = n-1
        end = n-1
        for i in range(1, C):
            if 0 <= n-1-i < n and 0 <= n-1+i < C:
                if arr[n-1-i] == arr[n-1+i]:
                    start = n-1-i
                    end = n-1+i
                else:
                    break

        for j in range(start, end+1):
            if arr[j] == 1:
                arr[j] = 0
            else:
                arr[j] = 1

for a in range(0, C, 20):
    print(*arr[a:a+20])