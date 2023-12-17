import sys
input = sys.stdin.readline

N = int(input())
x, y, i, z = 1, 1, 1, 1
while i < N:
    z = (x + y) % 15746 

    x = y
    y = z
    i += 1

print(z)