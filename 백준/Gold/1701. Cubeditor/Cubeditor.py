import sys
input = sys.stdin.readline

def kmp_pattern (p):

    L = len(p)
    F = [0] * L

    i = 1
    j = 0

    while i < L:

        if p[i] == p[j]:
            F[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = F[j-1]
        else:
            i += 1

    return F

S = input().rstrip()
answer = 0
for i in range(len(S)-1):
    K = S[i:]
    table = kmp_pattern(K)
    answer = max(answer, max(table))
print(answer)