import sys
input = sys.stdin.readline

S = input().rstrip()
total = float('inf')
if len(S) == 1:
    total = 1
    
for i in range(len(S)):
    K = S[i:]
    if K == K[::-1]:
        if len(K) < len(S):
            total = min(total, len(K) + 2 * (len(S) - len(K)))
        elif len(K) == len(S):
            total = len(S)
            break

print(total)
