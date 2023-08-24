import sys
input = sys.stdin.readline

N, M = map(int, input().split())
train = [[0] * 20 for _ in range(N)]

for _ in range(M):
    orders = [int(x) for x in input().split()]
    order = orders[0]
    train_num = orders[1]
    seat = orders[-1]

    if order == 1:
        train[train_num-1][seat-1] = 1

    if order == 2:
        train[train_num-1][seat-1] = 0

    if order == 3:

        train[train_num-1] = [0] + train[train_num-1][0:19]

    if order == 4:
        train[train_num - 1] = train[train_num - 1][1:20] + [0]

com = list()
for k in range(0, N):
    if train[k] not in com:
        com.append(train[k])
print(len(com))
