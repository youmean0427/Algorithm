import sys, math
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(float(input()))

for i in range(1, N):
    arr[i] = max(arr[i], arr[i-1] * arr[i])
print('%.3f' % max(arr))
# print(round(max(arr), 3))