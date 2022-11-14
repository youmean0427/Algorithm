arr = list(map(int, input().split()))
# print(arr)
num = [1, 2, 3, 4, 5, 6, 7, 8]

if arr == num[:]:
    print('ascending')
elif arr == num[::-1]:
    print('descending')
else:
    print('mixed')