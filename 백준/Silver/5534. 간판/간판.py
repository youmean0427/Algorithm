import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
ans = 0

for _ in range(n):
    k = input().strip()
    idx = 0
    check = 0
    while (idx < len(k)):
        if (s[0] == k[idx]):
            inter = 1
            while (inter < len(k)):
                temp = idx + inter
                last = 1
                sdx = 1
                while (last < len(k) and temp < len(k) and sdx < len(s)):
                    if (k[temp] == s[sdx]):
                        sdx += 1
                        temp = temp + inter
                    else:
                        break
                    last += 1
                if (sdx == len(s)):
                    check = 1
                inter += 1
        idx += 1
    if (check):
        ans += 1
print(ans)