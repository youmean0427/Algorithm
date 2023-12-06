import sys
input = sys.stdin.readline


S = input().rstrip()

arr = {"ABC" : 3, "DEF" : 4, "GHI" : 5, "JKL" : 6, "MNO" : 7, "PQRS" : 8, "TUV" : 9, "WXYZ" : 10}
answer = 0
for i in S:
    for x in arr:
        if i in x:
            answer += arr[x]

print(answer)