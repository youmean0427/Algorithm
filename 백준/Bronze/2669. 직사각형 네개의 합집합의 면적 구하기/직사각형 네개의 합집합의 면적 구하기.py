list_1 = [list(map(int, input().split())) for _ in range(4)]

# print(list_1)

x, y = [], []
for i in list_1:
    x.append(i[0])
    x.append(i[2])
    y.append(i[1])
    y.append(i[3])

# print(max(x), max(y)) # x의 범위, y의 범위

arr = [[0]*(max(y)+1) for _ in range(max(x)+1)]
# print(arr) # x, y의 범위로 좌표 만들기

for m in list_1:
    for k in range(m[0], m[2]):
        for n in range(m[1], m[3]):
            arr[k][n] = 1       
            # 좌표 영역 색칠하기 
            # 겹치는 부분 고려
            # 리스트는 좌표, 문제는 칸 기준이기 때문에 범위에 1을 더하지 않음

result = 0
for b in arr:
    result += sum(b)        # 색칠한 부분 모두 더하기
# print(arr)
print(result)