import sys
input = sys.stdin.readline

N, H = map(int, input().split())
top_arr = [0] * (H+1)
btm_arr = [0] * (H+1)

for i in range(1, N+1):
    if i % 2 == 0:
        btm_arr[int(input())] += 1
    else:
        top_arr[int(input())] += 1

for i in range(H-1, 0, -1):
    top_arr[i] = top_arr[i] + top_arr[i+1]
    btm_arr[i] = btm_arr[i] + btm_arr[i+1]

top_arr = top_arr[H+1:0:-1]
btm_arr = btm_arr[1::]

sum_arr = [0] * H
for i in range(H):
    sum_arr[i] = top_arr[i] + btm_arr[i]

min_val = min(sum_arr)
min_cnt = sum_arr.count(min_val)

print(min_val, min_cnt)