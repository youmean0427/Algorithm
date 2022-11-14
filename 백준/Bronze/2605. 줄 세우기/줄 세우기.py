N = int(input())
ch_num = list(map(int, input().split()))
# print(ch_num)

final = []
num = 1
while ch_num:
    cnt = ch_num.pop(0)
    if cnt == 0:
        final.append(num)
    else:
        final.append(num)
        while cnt:
            b = final.index(num)
            final[b-1], final[b] = final[b], final[b-1]

            cnt -= 1
    num += 1


print(*final)
