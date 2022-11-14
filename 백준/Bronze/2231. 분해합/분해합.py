N = int(input())
ans = 0
for i in range(1, 1000000):
    kk = str(i)
    result = i
    for j in range(len(kk)):
        result += int(kk[j])
    if result == N:
        ans = i
        break

print(ans)