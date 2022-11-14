K = int(input())
arr = list(map(int, input().split()))


def order(n):
    global l
    if n <= max(arr):
        order(2*n)
        result[n] = arr[l]
        l += 1
        order(2*n+1)

l = 0
result = [0] * (2**K + 1)
order(1)
# print(result)

for i in range(1,K+1):
    for k in range(2**(i-1), 2*(2**(i-1))):
        if result[k]:
            print(result[k], end= ' ')
    print()