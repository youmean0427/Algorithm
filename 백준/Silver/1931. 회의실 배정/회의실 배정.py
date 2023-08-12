import sys
input = sys.stdin.readline

T = int(input())
time = []
for j in range(T):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda x: (x[1], x[0]))
# print(time)

count = 1
end = time[0][1]
for i in range(1, T):
    if time[i][0] >= end:
        count += 1
        end = time[i][1]

print(count)