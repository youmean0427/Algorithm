import sys
input = sys.stdin.readline

S = input().rstrip()
arr = []

for i in S:

    arr.append(i)
    if len(arr) >= 3:
        if arr[-3] + arr[-2] + arr[-1] == "chu":
            arr[-3] = ""
            arr[-2] = ""
            arr[-1] = ""

    if len(arr) >= 2:
        if arr[-2] + arr[-1] == "pi":
            arr[-2] = ""
            arr[-1] = ""

        elif arr[-2] + arr[-1] == "ka":
            arr[-2] = ""
            arr[-1] = ""

if arr.count("") == len(S):
    print("YES")
else:
    print("NO")