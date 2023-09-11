import sys
input = sys.stdin.readline

L = int(input())
arr = [int(x) for x in input().split()]
N = int(input())

arr.sort()
flag = True
index = 0
start = 0

while flag:

    if N >= arr[index]:
        start = arr[index]
        index += 1
    elif N <= arr[index]:
        end = arr[index]
        flag = False

nums = []
for i in range(start+1, end):
    nums.append(i)

cnt = 0
for k in range(len(nums)):
    for j in range(k+1, len(nums)):
        a = nums[k]
        b = nums[j]

        if a <= N <= b:
            cnt += 1

print(cnt)