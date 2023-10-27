import sys
input = sys.stdin.readline

N = int(input())
arr = []
left = 0
right = 0
for _ in range(N):

    x = int(input())
    arr.append(x)

left_val, right_val = 0, 0

for i in range (len(arr)):

   if left_val < arr[i]:
       left += 1
       left_val = arr[i]

   if right_val < arr[-i-1]:
       right += 1
       right_val = arr[-i-1]

print(left)
print(right)