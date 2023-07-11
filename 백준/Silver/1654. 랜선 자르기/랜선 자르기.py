import sys

input=sys.stdin.readline


K, N = map(int, input().split())

total = 0
stick = list()
for _ in range(K):

    cm = int(input())
    stick.append(cm)

start, end = 1, max(stick)

while start <= end:

    mid = (start+end) // 2
    # print(start, end, mid)
    count = 0
    for i in stick:
        count += i // mid
    # print(count)


    if count < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)