import sys
input = sys.stdin.readline

N = int(input())

start = 1
end = 1
sm = 1
ans = 1

while end < N:

    if sm < N:
        end += 1
        sm += end
    elif sm > N:
        sm -= start
        start += 1
    else:
        ans += 1
        end += 1
        sm += end

print(ans)