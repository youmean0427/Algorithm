N = int(input())
arr = []
for i in range(N):
    x, y = input().split()
    x = int(x)

    arr.append((x, y))

arr = sorted(arr, key=lambda x: x[0])
# print(arr)
for i in arr:
    print(i[0], i[1])