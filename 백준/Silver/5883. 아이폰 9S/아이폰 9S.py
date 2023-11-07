import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

b_set = set(arr)
b_set.add(0)
answer = 0

for i in b_set:

    result = []
    for j in arr:
        if i == j:
            pass
        else:
            result.append(j)

    cnt = 1
    for n in range(len(result)-1):
        if result[n] == result[n+1]:
            cnt += 1
        else:
            answer = max(cnt, answer)
            cnt = 1

    answer = max(cnt, answer)

print(answer)