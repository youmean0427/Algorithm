N = int(input())
arr = list(map(int, input().split()))

# print(arr)
max_score = max(arr)
result = []
for i in arr:
    result.append(i/max_score * 100)

print(sum(result)/len(result))