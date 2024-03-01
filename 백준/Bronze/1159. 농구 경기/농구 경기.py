import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
cnt = {}
answer = []

for _ in range(N):
    S = input().rstrip()
    first = S[0]
    if first in cnt:
        cnt[first] += 1
    else:
        cnt[first] = 1

for i in cnt:
    if cnt[i] >= 5:
        answer.append(i)

answer.sort()
if answer:
    for ans in answer:
        print(ans, end="")
else:
    print("PREDAJA")