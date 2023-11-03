import sys
input = sys.stdin.readline

R, C, W = map(int, input().split())
arr = [[0], [1], [1, 1], [1, 2, 1]]

for i in range(3, R+W):
    box = [1]
    for j in range(len(arr[i])-1):
        box.append(arr[i][j]+arr[i][j+1])
    box.append(1)
    arr.append(box)

result = arr[R][C-1]
for l in range(1, W):
    result += sum(arr[l+R][C-1:l+C])

print(result)
