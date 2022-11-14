N = int(input())  # 100
len_result = 0
final_result = []
result = []


for i in range(1, N+1):
    result = [N]
    result.append(i)
    # print(result)
    while True:
        result.append(result[-2]-result[-1])

        if result[-2] - result[-1] < 0:
            break

    if len(result) > len_result:
        len_result = len(result)
        final_result = result

print(len_result)
print(*final_result)
