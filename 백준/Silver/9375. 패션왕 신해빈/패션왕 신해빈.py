import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr =[]
    cloth = {}

    for _ in range(N):
        a, b = map(str, input().split())
        arr.append((a, b))

    for word in arr:
        if word[1] in cloth:
            cloth[word[1]] += 1
        else:
            cloth[word[1]] = 1

    total = 1
    for k in cloth:
        total *= (cloth[k]+1)

    print(total-1)