import sys, math
input = sys.stdin.readline

def palindrom(s, start, end, cnt):
    cnt += 1
    if start >= end:
        return (1, cnt)
    elif s[start] != s[end]:
        return (0, cnt)
    else:
        return palindrom(s, start+1, end-1, cnt)

N = int(input())
for _ in range(N):
    S = input().rstrip()
    x = palindrom(S, 0, len(S)-1, 0)
    print(*x)
