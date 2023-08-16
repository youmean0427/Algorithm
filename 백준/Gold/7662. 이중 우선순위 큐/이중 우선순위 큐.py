import sys

input = sys.stdin.readline

import heapq  # 최소 힙

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    k = int(input())  # 연산 개수
    max_heap = []
    min_heap = []
    visited = [False for i in range(k + 1)]  # ★★index번째를 visited에 담는다!!! ★★ k개 입력됨
    lenn = 0

    for i in range(k):
        string, n = map(str, input().split())
        n = int(n)
        if string == 'I':
            lenn += 1
            heapq.heappush(max_heap, (-1 * n, i))  # (값,index)를 같이 담아준다!!! 중복된 값을 피하기 위함!
            heapq.heappush(min_heap, (n, i))
            visited[i] = True  # 해당 인덱스는 어느 힙에서도 삭제되지 않았고 사용 가능

        else:
            if lenn == 0:
                continue
            else:
                lenn -= 1
                if n == 1:  # max_heap에서 삭제
                    while True:
                        tmp = heapq.heappop(max_heap)
                        if visited[tmp[1]] == True:  # 삭제되지 않은 것을 사용할 것
                            visited[tmp[1]] = False
                            break

                else:  # min_heap에서 삭제
                    while True:
                        tmp = heapq.heappop(min_heap)
                        if visited[tmp[1]] == True:  # 삭제되지 않은 것을 사용할 것
                            visited[tmp[1]] = False
                            break

    if lenn == 0:
        print("EMPTY")
    else:
        while True:

            a = heapq.heappop(max_heap)
     
            if visited[a[1]] == True:  # 삭제되지 않은 것을 사용할 것
                break
        while True:
            b = heapq.heappop(min_heap)
            if visited[b[1]] == True:  # 삭제되지 않은 것을 사용할 것
                break
        print(a[0] * -1, b[0])

