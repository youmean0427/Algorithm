import sys, heapq
# sys.stdin = open('EX.txt', 'r')
input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    num = int(input())

    if num > 0:
        heapq.heappush(heap, -num)
    elif num == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        print(0)