N, M = map(int, input().split())

num_list = list(map(int, input().split()))

# print(num_list)
result_list = []
num_list.sort(reverse=True)
# print(num_list)
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            result = num_list[i] + num_list[j] + num_list[k]
            # print(result)
            if result <= M:
                result_list.append(result)

result_list.sort()
print(result_list[-1])
# print(result_list[-1])