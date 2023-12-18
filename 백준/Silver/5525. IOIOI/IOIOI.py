import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
P = 'IOI' + 'OI' * (N-1)
K = [0] * len(P)

def pattern (S):

    i = 0
    j = 1
    while j < len(S):
        if S[i] == S[j]:
            K[j] = i + 1
            i += 1
            j += 1
        else:
            j += 1

pattern(P)
cnt = 0

def KMP(P, S):

    global cnt
    i = 0
    j = 0
    while i < len(S):

        if S[i] == P[j]:
            if j == len(P) - 1:
                cnt += 1
                j = K[j-1]
            else:
                i += 1
                j += 1

        else:
            if j > 0:
                j = K[j-1]
            else:
                i += 1

KMP(P, S)
print(cnt)
