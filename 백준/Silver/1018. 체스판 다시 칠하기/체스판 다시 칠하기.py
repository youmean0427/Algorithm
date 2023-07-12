M, N = map(int, input().split())

arr = [list(input()) for _ in range(M)]

box1 = list()
box2 = list()

result = list()

def check (arr, row, col, black, white):
    count = 0

    for n in range(8):
        for m in range(8):
            if arr[row][col] == black:
                if m % 2 == n % 2:
                    if arr[n][m] == white:
                        count += 1

                if m % 2 != n % 2:
                    if arr[n][m] == black:
                        count += 1

            if arr[row][col] == white:
                if m % 2 == n % 2:
                    if arr[n][m] == black:
                        count += 1

                if m % 2 != n % 2:
                    if arr[n][m] == white:
                        count += 1

    result.append(count)

for i in range(M-7):
    for j in range(N-7):
        for k in range(i, i+8):
            for l in range(j, j+8):
                box1.append(arr[k][l])
            box2.append(box1)
            box1 = list()
        check(box2, 0, 0, 'B', 'W')
        check(box2, 7, 7, 'B', 'W')
        check(box2, 0, 7, 'W', 'B')
        check(box2, 7, 0, 'W', 'B')
        box2 = list()

print(min(result))