import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

time = 0
power = 0
work = 0
while time < 24:

    if power + A <= M:
        time += 1
        power += A
        work += B
    else:
        time += 1
        power -= C
        if power < 0:
            power = 0

print(work)
