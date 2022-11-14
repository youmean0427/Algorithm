import math

N, K = map(int, input().split())
girl = [0] * 7
boy = [0] * 7
room = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        girl[b] += 1
    else:
        boy[b] += 1
# print(girl, boy)

for i in girl:
    if i <= K and i > 0:
        room += 1
    elif i > K:
        room += math.ceil(i/K)

for i in boy:
    # print(i)
    if i <= K and i > 0:
        room += 1
    elif i > K:
        room += math.ceil(i/K)

print(room)
