T = int(input())
box = list()

for i in range(T) :
    a, b = map(int, input().split())
    box.append((a, b))

check = [['-' for _ in range(T)] for _ in range(T)]

for k in range(T):
    for m in range(T):

        if box[k][0] > box[m][0] and box[k][1] > box[m][1]:
           check[k][m] = 'X'
        elif box[k][0] < box[m][0] and box[k][1] < box[m][1]:
            check[k][m] = 'O'

result = list()
for i in check:
    result.append(str(i.count('O')+1))

final = ' '.join(result)
print(final)