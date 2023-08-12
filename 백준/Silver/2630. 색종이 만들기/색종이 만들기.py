import sys
input = sys.stdin.readline

T = int(input())
arr = [[int(x) for x in input().split()] for _ in range(T)]

result = [0, 0]
def paper (x, y, T):
    check = []

    for i in range(T):
        for j in range(T):
            check.append(arr[x+i][y+j])
            
    if check.count(1) == T ** 2:
        result[1] += 1
    elif check.count(0) == T ** 2:
        result[0] += 1
    else:
        T = T // 2
        paper(x, y, T)
        # print("-----")
        paper(x, y+T, T)
        # print("-----")
        paper(x+T, y, T)
        # print("-----")
        paper(x+T, y+T, T)

    return result

answer = paper(0, 0, T)
print(answer[0])
print(answer[1])