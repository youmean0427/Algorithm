import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
arr = [i for i in range(N+1)]

if len(arr) <= 2:
    box = arr
while len(arr) > 2:
    box = []
    for i in range(len(arr)):
        if i % 2 == 0:
            box.append(arr[i])
    arr = box

print(box[1])