import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
    N = int(input())


    if N > 11:
        for i in range(1, N-9):
            arr.append(arr[9+i] + arr[5+i])
        print(arr[N-1])

    else:
        print(arr[N-1])