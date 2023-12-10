import sys
input = sys.stdin.readline

S = input().rstrip()
S_set = set()
i = 0
j = 1

while i < len(S):
    while j < len(S)+1:
        S_set.add(S[i:j])
        j += 1
    i += 1
    j = i+1

print(len(S_set))

