import sys
input = sys.stdin.readline

N = int(input())
cnt = N
for _ in range(N):
    S = input().rstrip()
    q = []

    for i in range(len(S)):
        if S[i] in q:
            if q[-1] != S[i]:
                cnt -= 1
                break
        else:
            q.append(S[i])
print(cnt)