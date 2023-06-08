L = int(input())
text = input()

case = 0
sum = 0

while case < L :
    for i in text:
        sum += (ord(i)-96) * (31 ** case)
        case += 1

print(sum)