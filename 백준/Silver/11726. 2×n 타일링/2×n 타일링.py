N = int(input())

arr = [0, 1, 2, 3]


for _ in range(N-3):
    arr.append(arr[-1] + arr[-2])
    # print(arr)

print(arr[N]%10007)