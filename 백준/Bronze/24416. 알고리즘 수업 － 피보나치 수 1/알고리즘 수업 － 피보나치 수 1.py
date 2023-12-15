import sys, math
input = sys.stdin.readline

N = int(input())
arr = [0] * (N+1)

def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)

def fibo_dp(n):
    arr[1] = 1
    arr[2] = 1
    cnt = 0
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
        cnt += 1
    return cnt

x = fibo_dp(N)
print(arr[N], x)