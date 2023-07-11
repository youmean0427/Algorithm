import sys
input = sys.stdin.readline

N = int(input())
arr = list()

for _ in range (N):
    score = int(input())
    arr.append(score)


def round_def (x):
    dot_index = str(x).index('.')
    if int(str(x)[dot_index+1]) >= 5:
        result = str(x)[:dot_index]
        result = int(result) + 1
    else:
        result = int(str(x)[:dot_index])

    return result

arr.sort()
avg = round_def(N * 0.15)

for i in range(avg):
    arr[i] = 0
for i in range(1, avg+1):
    arr[-i] = 0

if N != 0:
    result = round_def((sum(arr)/(len(arr)-arr.count(0))))
elif N == 1 or N == 2:
    result = 0
else:
    result = 0
print(result)
