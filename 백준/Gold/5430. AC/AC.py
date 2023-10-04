import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):

    p = input().rstrip()
    n = int(input())
    char = input().rstrip()
    arr = deque(char[1:-1].split(","))


    check = 0
    del_count = 0

    if n == 0:
        arr = []

    for i in p:

        if i == "R":
            if del_count == 0:
                del_count = 1
            else:
                del_count = 0


        elif i == "D":
            if len(arr) < 1:
                check = 1
                print("error")
                break

            if del_count == 0:
                arr.popleft()

            elif del_count == 1:
                arr.pop()


    if check == 0:
        if del_count == 1:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("[" + ",".join(arr) + "]")
