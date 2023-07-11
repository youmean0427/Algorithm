T = int(input())
num = 666
count = 1

while True:

    if count == T:
        break

    num += 1
    if '666' in str(num):
        count +=1

print(num)