T = int(input())

for _ in range(T):

    k = int(input())
    n = int(input())

    arr = [[0] * n for _ in range(k+1)]

    for i in range(n):
        arr[0][i] = i + 1

    for j in range(1, k+1):
        for k in range(0, n):
            for l in range(k+1):
                arr[j][k] += arr[j-1][l]

    print(max(max(arr)))