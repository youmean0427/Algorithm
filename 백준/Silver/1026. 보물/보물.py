N = int(input())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

# print(a_arr,b_arr)

a_arr.sort()
b_arr.sort(reverse=True)

result = 0
for i in range(len(a_arr)):
    result += a_arr[i] * b_arr[i]

print(result)