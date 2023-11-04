import sys

input = sys.stdin.readline

x, y, c = map(float, input().split())

start = 0
end = min(x, y)

while start <= end:

    mid = (start + end) / 2

    h1 = ((x ** 2) - (mid ** 2)) ** (1 / 2)
    h2 = ((y ** 2) - (mid ** 2)) ** (1 / 2)
    hh = (h1 * h2) / (h1 + h2)
    if c-0.001 < round(hh, 3) < c+0.001:
        print(round(mid, 3))
        exit()
    elif hh > c:
        start = mid
    else:
        end = mid