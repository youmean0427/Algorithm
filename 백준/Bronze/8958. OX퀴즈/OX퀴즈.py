N = int(input())
for i in range(N):
    arr = list(input())

    count = 0
    next = 0
    for k in arr:
        if k == 'O' and next == 0:
            count += 1
            next = 1
        elif k == 'O' and next >= 1:
            count += 1 + next
            next += 1
        elif k == 'X':
            next = 0

    print(count)
