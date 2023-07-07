T = int(input())

result = T

for i in range (1, (T // 3)+1):

    num2 = T - 3 * i

    if num2 % 5  == 0:

        if result > i + (num2 // 5):
            result = i + (num2 // 5)


for k in range(1, (T//5)+1):

    num3 = T - 5 * k

    if num3 % 3 == 0 :

        if result > k + (num3 // 3):
            result = k + (num3 // 3)

if result == T:
    result  = -1

print(result)