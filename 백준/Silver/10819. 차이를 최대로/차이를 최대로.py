import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

x = list(permutations(arr, N))
answer = 0

def check(arr):
    global answer
    result = 0
    for i in range(len(arr)-1):
        result += abs(arr[i] - arr[i+1])

    answer = max(result, answer)

for i in x:
    check(i)

print(answer)