import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = []
c = []
result = 0
for _ in range(N):
    s.append(input().rstrip())

for _ in range(M):
    c = input().rstrip()
    if c in s:
        result += 1

print(result)