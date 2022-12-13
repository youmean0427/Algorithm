N = int(input())

arr = list(map(int, input().split()))
final_count = 0
for i in arr:
    count = 0
    for k in range(1, i+1):
        # print(i/k)

        if str(i/k)[-1] == str(0):
            count += 1

    if count == 2:
        final_count += 1

print(final_count)