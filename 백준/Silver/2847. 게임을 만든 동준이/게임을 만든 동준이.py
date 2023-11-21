import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr = arr[::-1]
answer = 0
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        x = arr[i]-1
        answer += arr[i+1] - x
        arr[i+1] = x
print(answer)
