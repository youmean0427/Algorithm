N = input()
result = [-1] * 26
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(N)-1,-1, -1):
    for k in alpha:
        if N[i] == k:
            result[alpha.index(k)] = i

print(*result)