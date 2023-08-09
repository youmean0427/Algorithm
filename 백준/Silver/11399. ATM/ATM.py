import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(x) for x in input().split())

total = 0
arr.sort()
for i in range(N):
    for j in range(0, i+1):
        total += arr[j]
print(total)
