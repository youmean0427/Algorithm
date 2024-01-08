import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[0] * 26 for _ in range(26)]

for _ in range(N):
    line = [i for i in input().split()]
    arr[ord(line[0])-97][ord(line[2])-97] = 1

for i in range(26):
    for j in range(26):
        for k in range(26):
            if arr[j][i] and arr[i][k]:
                arr[j][k] = 1

M = int(input())
for _ in range(M):
    line = [i for i in input().split()]
    if arr[ord(line[0])-97][ord(line[2])-97]:
        print('T')
    else:
        print('F')
