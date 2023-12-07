import sys
input = sys.stdin.readline

N = 9
max_value = 0
ij = [1, 1]

for i in range(1, N+1):
    j = 1
    for x in input().split():
        if max_value < int(x):
            max_value = int(x)
            ij = [i, j]
        j += 1

print(max_value)
print(*ij)
