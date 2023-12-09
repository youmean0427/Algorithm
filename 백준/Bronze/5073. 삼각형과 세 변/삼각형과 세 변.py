import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    arr = [a, b, c]
    if a == 0:
        break

    arr.sort()
    if arr[-1] < arr[0] + arr[1]:
        if a == b == c:
            print("Equilateral")
        elif (a == b or b == c or a == c):
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")