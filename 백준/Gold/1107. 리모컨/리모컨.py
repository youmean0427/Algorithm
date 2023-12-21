import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N = input().rstrip()
N = '0' + N
M = int(input())
bnt = []
if M:
    bnt = set(map(int, input().split()))

start = 100
ans = abs(int(N) - start)

def back(n, sm):
    global ans

    if n == len(N):
        ans = min(ans, (abs(int(N) - int(sm))) + len(str(int(sm))))
        return

    for i in range(10):
        if i in bnt:
            if i == 0:
                if (len(sm) >= 1 and sm[n-1] == '0' and n != len(N)-1) or n == 0:
                    back(n + 1, sm + '0')
        else:
            back(n+1, sm + str(i))

back(0, '')
print(ans)