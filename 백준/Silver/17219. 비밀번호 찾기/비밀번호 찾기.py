import sys

input = sys.stdin.readline
# sys.stdin = open("EX.txt", "r")

N, M = map(int, input().split())

arr = {}
for _ in range(N):
    mail, password = map(str, input().split())
    arr[mail] = password

result = []
for _ in range(M):
    check_mail = input().rstrip()
    if check_mail in arr:
        result.append(arr[check_mail])

for i in result:
    print(i)