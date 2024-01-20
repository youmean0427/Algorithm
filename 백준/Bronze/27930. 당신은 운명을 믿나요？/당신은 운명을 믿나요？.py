import sys
input = sys.stdin.readline

S = list(i for i in input().rstrip())

korea = "KOREA"
yonsei = "YONSEI"
k_idx = 0
y_idx = 0

while S:
    x = S.pop(0)

    if korea[k_idx] == x:
        k_idx += 1
    if yonsei[y_idx] == x:
        y_idx += 1


    if k_idx == 5:
        print(korea)
        break
    if y_idx == 6:
        print(yonsei)
        break

