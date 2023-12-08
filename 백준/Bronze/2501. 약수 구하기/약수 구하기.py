import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 1
answer = 0
for i in range(1, N+1):
    if N % i == 0:
        if cnt == K:
            answer = i
            break
        cnt += 1

print(answer)