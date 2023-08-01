import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
result = []

for _ in range(N):
    name = input()
    arr.append(name[:len(name)-1])

for _ in range(M):
    name = input()
    result.append(name[:len(name)-1])

arr = set(arr)
result = set(result)
result = arr & result
result = list(result)

result.sort()
print(len(result))
for i in result:
    print(i)