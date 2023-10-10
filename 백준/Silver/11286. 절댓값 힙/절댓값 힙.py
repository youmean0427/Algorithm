import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
cnt = 0
for _ in range(N):
    x = int(input())
    if x != 0:
        if x < 0:
            heapq.heappush(heap, [abs(x), -1])
        else:
            heapq.heappush(heap, [abs(x), 1])
    else:
        if heap:
            y, z = heapq.heappop(heap)
            print(y*z)
        else:
            print(0)