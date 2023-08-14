import sys
input = sys.stdin.readline

n = int(input())

arr = [0, 1, 3, 5, 11, 21]
check = [1, -1]

for i in range(6, n+1):
    cnt = arr[i - 1] * 2
    if i % 2 == 0:
        cnt += check[0]
        arr.append(cnt)
    else:
        cnt += check[1]
        arr.append(cnt)

print(arr[n] % 10007)