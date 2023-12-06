import sys
input = sys.stdin.readline

S = [x for x in input().rstrip()] + ["0"]
alpha = ["c=", 'c-', "d-", "lj", "nj", "s=", "z="]

i = 0
j = 1
cnt = 0

while j < len(S):

    if S[i] == "d" and S[j] == 'z':
        j += 1

        if "".join(S[i:j+1]) == "dz=":
            cnt += 1
            i += 3
            j += 2
            continue
        else:
            cnt += 1
            i += 1
            continue

    find = S[i] + S[j]
    if find in alpha:
        cnt += 1
        i += 2
        j += 2
    else:
        cnt += 1
        i += 1
        j += 1

print(cnt)