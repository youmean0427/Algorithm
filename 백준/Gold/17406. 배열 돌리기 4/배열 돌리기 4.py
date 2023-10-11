from collections import deque
import copy
from itertools import permutations

def turn(arr, r, c, s):

    sr = r-s-1
    sc = c-s-1
    er = r+s-1
    ec = c+s-1

    N = er-sr+1
    M = ec-sc+1



    for i in range((min(M,N)// 2)):
        q = deque()

        q.extend(arr[sr+i][sc+i:ec+1-i])
        q.extend(x[ec-i] for x in arr[sr+1+i:er-i])
        q.extend(arr[er-i][sc+i:ec+1-i][::-1])
        q.extend(x[sc+i] for x in arr[sr+1+i:er-i][::-1])

        q.rotate(1)

        for j in range(sc+i, ec-i+1):
            arr[sr+i][j] = q.popleft()
        for j in range(sr+i+1, er-i):
            arr[j][ec-i] = q.popleft()


        for j in range(ec-i, sc+i-1, -1):
            arr[er-i][j] = q.popleft()

        for j in range(er-i-1, sr+i, -1):
            arr[j][sc+i] = q.popleft()

    return arr


N, M, K = map(int, input().split())

arr = [[int(x) for x in input().split()] for _ in range(N)]

info = []
for _ in range(K):
    r, c, s = map(int, input().split())
    info.append((r,c,s))

info = list(permutations(info, len(info)))
box = []
for j in info:
    o_arr = copy.deepcopy(arr)
    for i in j:

        result = turn(o_arr, i[0], i[1], i[2])

    for i in result:
        box.append(sum(i))

print(min(box))

