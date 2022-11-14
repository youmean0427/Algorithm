num = 1
for _ in range(3):
    num2 = int(input())
    num *= num2
num_list = [0] * 10

for i in str(num):
    num_list[int(i)] += 1

for i in num_list:
    print(i)