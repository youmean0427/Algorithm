import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s_arr = []
for i in arr:
    if i in s_arr:
        continue
    else:
        s_arr.append(i)

def back(cnt, sm):

    if (cnt == M):
        print(*sm)
        return

    for i in s_arr:
        if ((sm and sm[-1] <= i) or len(sm) == 0):
            sm.append(i)
            back(cnt+1, sm)
            sm.pop()

back(0, [])