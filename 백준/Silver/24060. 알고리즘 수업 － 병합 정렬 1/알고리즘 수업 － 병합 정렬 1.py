import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
arr = [int(i) for i in input().split()]

cnt = []
def merge(x):

    if len(x) == 1:
        return x

    n = math.ceil(len(x) / 2)
    left_arr = x[:n]
    right_arr = x[n:]

    left_sort = merge(left_arr)
    right_sort = merge(right_arr)

    li = 0
    ri = 0
    merge_sort = []
    while li < len(left_sort) and ri < len(right_sort):
        if left_sort[li] < right_sort[ri]:
            merge_sort.append(left_sort[li])
            cnt.append(left_sort[li])
            li += 1
        else:
            merge_sort.append(right_sort[ri])
            cnt.append(right_sort[ri])
            ri += 1

    merge_sort += left_sort[li:]
    merge_sort += right_sort[ri:]
    for i in left_sort[li:]:
        cnt.append(i)
    for j in right_sort[ri:]:
        cnt.append(j)

    return merge_sort

merge(arr)
if K > len(cnt):
    print(-1)
else:
    print(cnt[K-1])