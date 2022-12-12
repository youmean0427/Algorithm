# 카운팅 정렬
import sys

N = int(sys.stdin.readline())

result = [0] * 10001

for _ in range(N):
    result[int(sys.stdin.readline())] += 1

for i in range(len(result)):
    while result[i]:
        print(i)
        result[i] -= 1
