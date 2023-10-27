import sys
input = sys.stdin.readline

N = input().rstrip()
arr = []

for i in N:
    arr.append(int(i))

arr.sort(reverse=True)

result = ''
for i in arr:
    result += str(i)
print(result)