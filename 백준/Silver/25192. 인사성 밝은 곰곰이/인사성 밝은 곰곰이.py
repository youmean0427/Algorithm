import sys, math
input = sys.stdin.readline

N = int(input())
result = set()
total = 0
for _ in range(N):
    x = input().rstrip()

    if x == "ENTER":
        total += len(result)
        result = set()
    else:
        result.add(x)

print(total + len(result))