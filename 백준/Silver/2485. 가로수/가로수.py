import sys, math
input = sys.stdin.readline

N = int(input())
arr = []
dis = []
for _ in range(N):
    x = int(input())
    if arr:
        dis.append(x - arr[-1])
    arr.append(x)

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

dis.sort()
step = float('inf')
for i in range(len(dis)):
    step = min(step, GCD(step, dis[i]))
end = max(arr)
start = min(arr)
print((math.ceil((end - start + 1) / step)) - N)
