import sys, heapq
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    heap = []
    J, N = map(int, input().split())

    for _ in range(N):
        R, C = map(int, input().split())
        heapq.heappush(heap, - (R * C))

    answer = 0
    while J > 0:
        x = -heapq.heappop(heap)
        J -= x
        answer += 1
    print(answer)