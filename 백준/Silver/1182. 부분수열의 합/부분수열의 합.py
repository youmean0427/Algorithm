N, S = map(int, input().split())
a = list(map(int, input().split()))

result = []
f_result = 0

for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & 1 << j:
            subset.append(a[j])
    result.append(subset)

result.pop(0)
for i in result:
    if sum(i) == S:
        f_result += 1

print(f_result)