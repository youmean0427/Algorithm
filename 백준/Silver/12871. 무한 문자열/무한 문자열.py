S = input()
T = input()

ans = 0

if len(T) > len(S):
    cnt = len(T) // len(S)
    if S * cnt == T or T * len(S) == S * len(T):
        ans = 1
else:
    cnt = len(S) // len(T)
    if T * cnt == S or T * len(S) == S * len(T):
        ans = 1

print(ans)