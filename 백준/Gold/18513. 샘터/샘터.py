import sys
from collections import defaultdict, deque
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
case = [(int(i), 0) for i in input().split()]

arr = defaultdict(int)

for i in range(len(case)):
    arr[case[i][0]] = 1

total = 0
count = 0
idx = 1

def bfs(start):
    global total, count

    q = deque(start)

    while q:
        x, y = q.popleft()
        if count >= K:
            return

        for i in [x+1, x-1]:
            if arr[i] == 0:
                arr[i] = 1
                count += 1
                total += y+1
                q.append((i, y+1))

                if count >= K:
                    return

bfs(case)
print(total)
