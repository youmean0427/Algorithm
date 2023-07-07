T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    check = [0] * N
    check[M] = 1

    count = 0
    flag = 1

    while flag:
        if q and check:
            while q[0] != max(q):
                for j in range(1, len(q)):
                    if q[0] < q[j]:
                        num = q.pop(0)
                        q.append(num)
                        num_check = check.pop(0)
                        check.append(num_check)
            q.pop(0)
            check.pop(0)
            count += 1

        if 1 not in check:
            flag = 0
            break

    print(count)