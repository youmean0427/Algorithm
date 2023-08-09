import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    result = []
    arr = list(char for char in input().split())

    # 비둘기집 원리
    if N > 32:
        print(0)
    else:
        arr_c = list(combinations(arr, 3))
        for n in arr_c:
            count = 0
            for i in range(3):
                for j in range(i+1, 3):
                    for k in range(4):
                        if n[i][k] != n[j][k]:
                            count += 1
            result.append(count)

        print(min(result))