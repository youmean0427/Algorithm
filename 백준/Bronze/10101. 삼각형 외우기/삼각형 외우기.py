import sys
input = sys.stdin.readline

arr = {}
total = 0
for _ in range(3):
    x = int(input())
    if x in arr:
        arr[x] += 1
        total += x
    else:
        arr[x] = 1
        total += x

if total == 180:
    if len(arr) == 1:
        print("Equilateral")
    elif len(arr) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")