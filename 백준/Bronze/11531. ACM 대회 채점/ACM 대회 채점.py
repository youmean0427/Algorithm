
d_count = {}
total = 0
cnt = 0
while (1):
    arr = input().split()
    arr[0] = int(arr[0])

    if (arr[0] == -1):
        break

    if (arr[2] == 'right'):
        if (arr[1] in d_count):
            total += arr[0] + d_count[arr[1]] * 20
        else:
            total += arr[0]
        cnt += 1
    else:
        if (arr[1] in d_count):
            d_count[arr[1]] += 1
        else:
            d_count[arr[1]] = 1
print(cnt, total)