from sys import stdin

N, M, B = map(int, stdin.readline().split())
heights = []
for _ in range(N):
    heights += list(map(int, stdin.readline().split()))

heights.sort(reverse=True)
minH = min(heights)
maxH = max(heights)
allCase = []

for i in range(minH, maxH + 1):
    time = 0
    height = i
    blocks = B

    for j in heights:
        if j < i:
            blocks -= (i - j)
            if blocks < 0:
                height = -1
                break

            time += (i - j)
        elif j > i:
            time += (j - i) * 2
            blocks += (j - i)

    if height == i:
        allCase.append([time, height])

temp = min(allCase, key=lambda x: (x[0], -x[1]))
print(str(temp[0]) + " " + str(temp[1]))