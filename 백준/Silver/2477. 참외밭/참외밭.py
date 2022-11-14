T = int(input()) # 참외
dir = []
leng = []
for _ in range(6):
    a, b = map(int, input().split())
    dir.append(a)
    leng.append(b)
# print(dir, leng)

maxx = leng[0]
for i in range(0, len(leng), 2):
    if maxx < leng[i]:
        maxx = leng[i]

maxy = leng[1]
for j in range(1, len(leng), 2):
    if maxy < leng[j]:
        maxy = leng[j]

# print(maxx * maxy)
total = maxx * maxy

dir.append(dir[0])
leng.append(leng[0])

for i in range(0, len(dir)-1):
    if dir[i] == 4 and dir[i+1] == 1:
        total -= leng[i] * leng[i+1]
    if dir[i] == 1 and dir[i+1] == 3:
        total -= leng[i] * leng[i + 1]
    if dir[i] == 2 and dir[i + 1] == 4:
        total -= leng[i] * leng[i + 1]
    if dir[i] == 3 and dir[i + 1] == 2:
        total -= leng[i] * leng[i + 1]

print(total * T)