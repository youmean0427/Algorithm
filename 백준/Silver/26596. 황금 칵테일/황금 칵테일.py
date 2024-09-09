import sys, math
input = sys.stdin.readline

n = int(input())
d = {}
for _ in range(n):
    a, b = input().split()
    if (a in d):
        d[a] += int(b)
    else:
        d[a] = int(b)

sort_d = sorted(d.items(), key=lambda x:x[1])
for k, v in sort_d:
    f = v * 1.618
    for kk, vv in sort_d:
        if (k == kk):
            continue
        if (vv == math.floor(f)):
            print("Delicious!")
            exit(0)
print("Not Delicious...")