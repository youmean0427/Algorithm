import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    start, end = map(int, input().split())
    cnt = 0
    for k in range(start, end+1):
        if '0' in str(k):
            cnt += str(k).count('0')

    print(cnt)