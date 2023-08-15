import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
char = input().rstrip()
arr = []

for x in char:
    arr.append(x)

IOI = ['IOI']

for i in range(1, N):
    IOI.append(IOI[i-1] + 'OI')

check_IOI = []
for j in IOI[N-1]:
    check_IOI.append(j)

cnt = 0
for k in range(0, M-len(check_IOI)+1):
    if check_IOI == arr[k:k+len(check_IOI)]:
        cnt += 1

print(cnt)