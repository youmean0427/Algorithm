N = int(input())
arr = []
for _ in range(N):
    arr.append(input())


answer = []
for i in range(len(arr[0])):
    cnt = set()
    for j in range(len(arr)):
        cnt.add(arr[j][i])

    if len(cnt) > 1:
        answer.append("?")
    else:
        answer.append(arr[j][i])
print("".join(answer))