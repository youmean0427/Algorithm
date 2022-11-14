x, y = map(int, input().split())
N = int(input())
store = []
for _ in range(N):
    a, b = map(int, input().split())
    store.append([a, b])
nx, ny = map(int, input().split())
now = [nx, ny]
# print(store)

count = 0

if now[0] == 1:
    for i in store:

        if i[0] == 1:
            aa = now[1] - i[1]
            if aa < 0:
                count += -aa
            else:
                count += aa

        if i[0] == 2:
            aa1 = now[1] + i[1] + y
            bb1 = x - now[1] + x - i[1] + y
            count += min(aa1, bb1)

        if i[0] == 3:
            aa1 = now[1] + i[1]
            count += aa1

        if i[0] == 4:
            aa1 = x - now[1] + i[1]
            count += aa1
    print(count)

if now[0] == 2:
    for i in store:

        if i[0] == 2:
            aa = now[1] - i[1]
            if aa < 0:
                count += -aa
            else:
                count += aa

        if i[0] == 1:
            aa1 = now[1] + i[1] + y
            bb1 = x - now[1] + x - i[1] + y
            count += min(aa1, bb1)

        if i[0] == 3:
            aa1 = now[1] + y - i[1]
            count += aa1

        if i[0] == 4:
            aa1 = x - now[1] + y - i[1]
            count += aa1
    print(count)

if now[0] == 3:
    for i in store:

        if i[0] == 3:
            aa = now[1] - i[1]
            if aa < 0:
                count += -aa
            else:
                count += aa

        if i[0] == 4:
            aa1 = now[1] + i[1] + x
            bb1 = y - now[1] + y - i[1] + x
            count += min(aa1, bb1)

        if i[0] == 1:
            aa1 = now[1] + i[1]
            count += aa1

        if i[0] == 2:
            aa1 = y - now[1] + i[1]
            count += aa1
    print(count)

if now[0] == 4:
    for i in store:

        if i[0] == 4:
            aa = now[1] - i[1]
            if aa < 0:
                count += -aa
            else:
                count += aa

        if i[0] == 3:
            aa1 = now[1] + i[1] + x
            bb1 = y - now[1] + y - i[1] + x
            count += min(aa1, bb1)

        if i[0] == 1:
            aa1 = now[1] + x - i[1]
            count += aa1

        if i[0] == 2:
            aa1 = y - now[1] + x - i[1]
            count += aa1
    print(count)