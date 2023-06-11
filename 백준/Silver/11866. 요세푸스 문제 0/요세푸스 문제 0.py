import sys
input=sys.stdin.readline

N, K = map(int, input().split())
arr = list()

for i in range (1, N+1):
    arr.append(i)

result = list()

count = K-1
while arr:
    count = count % len(arr)
    result.append(arr.pop(count))
    count += K-1

newList = [str(a) for a in result]
print("<", ", ".join(newList), ">", sep='')