import sys
input = sys.stdin.readline

S = list(input().rstrip())

i = 0
start = 0

while i < len(S):

    if S[i] == '<':
        i += 1
        while S[i] != ">":
            i += 1
        i += 1
    elif S[i].isalnum():
        start = i
        while i < len(S) and S[i].isalnum():
            i += 1
        sub = S[start:i]
        sub.reverse()
        S[start:i] = sub
    else:
        i += 1

print("".join(S))