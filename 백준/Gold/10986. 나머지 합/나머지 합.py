import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(i) for i in input().split()]

prefix_sum = 0
count_mod_m = {0: 1}  # 누적 합의 나머지 값과 해당 값의 개수를 저장하는 딕셔너리

cnt = 0
for i in range(N):

    prefix_sum = (prefix_sum + arr[i]) % M
    if prefix_sum in count_mod_m:
        cnt += count_mod_m[prefix_sum]
        count_mod_m[prefix_sum] += 1
    else:
        count_mod_m[prefix_sum] = 1

print(cnt)