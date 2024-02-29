import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
check = [False] * (N+1)
ans = []
for i in range(2, N+1):
    if check[i] == False:
        check[i] = True
        ans.append(i)
        for j in range(i+i, N+1, i):
            if check[j] == False:
                check[j] = True
                ans.append(j)
print(ans[K-1])
