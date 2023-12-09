import sys
input = sys.stdin.readline

N, B = map(int, input().split())
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = []
while N >= B:
    x.append(N % B)
    N = N // B

x.append(N)
x.reverse()
answer = ''
for i in x:
    answer += arr[i]
print(answer)