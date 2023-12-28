import sys
input = sys.stdin.readline
from itertools import combinations

def back(n, sm):
    global max_val, min_val

    if n >= N:
        max_val = max(max_val, sm)
        min_val = min(min_val, sm)
        return

    for i in range(len(op)):
        if op[i]:
            if i == 0:
                op[i] -= 1
                back(n + 1, sm + arr[n])
                op[i] += 1
            elif i == 1:
                op[i] -= 1
                back(n + 1, sm - arr[n])
                op[i] += 1
            elif i == 2:
                op[i] -= 1
                back(n + 1, sm * arr[n])
                op[i] += 1
            elif i == 3:
                op[i] -= 1
                if sm < 0:
                    back(n + 1, -(-sm // arr[n]))
                else:
                    back(n + 1, sm // arr[n])
                op[i] += 1


N = int(input())
arr = [int(x) for x in input().split()]
op = [int(x) for x in input().split()]

max_val = -float('inf')
min_val = float('inf')
back(1, arr[0])

print(max_val, min_val)