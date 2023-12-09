import sys
input = sys.stdin.readline

X = int(input())

i = 0
total = 0

while total < X:
    i += 1
    total += i

start = (X - (total - i))

n = 1
m = i
if i % 2 == 0:
    for a in range(1, start):
        n += 1
        m -= 1
    print(f'{n}/{m}')
else:
    for a in range(i, start, -1):
        n += 1
        m -= 1
    print(f'{n}/{m}')
