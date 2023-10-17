import sys
input = sys.stdin.readline

arr = [[x for x in input().rstrip()] for _ in range(5)]

max_len = 0
for i in arr:
    max_len = max (max_len, len(i))

result = ''
for i in range(max_len):
    for j in range(len(arr)):
        try:
            result += arr[j][i]
        except:
            pass

print(result)
