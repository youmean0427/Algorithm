import sys
input = sys.stdin.readline

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]
answer = {-1: 0, 0: 0, 1: 0}

def check (arr):
    val = arr[0][0]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != val:
                return "divide"

    return val

def divide(arr,N):

    for k in range(0, N, N//3):
        for j in range(0, N, N//3):
            divided_arr = []

            for i in range(k, k+N//3):
                divided_arr.append(arr[i][j:j+N//3])

            x = check(divided_arr)
            if x == "divide":
                divide(divided_arr, N//3)
            else:
                answer[x] += 1

if N == 1:
    answer[arr[0][0]] += 1
else:
    if check(arr) == 'divide':
        divide(arr, N)
    else:
        answer[check(arr)] += 1

print(answer[-1])
print(answer[0])
print(answer[1])