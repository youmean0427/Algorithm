N = int(input())

i = 1
line = 1
k = 6
if N == 1:
    print(1)
else:
    while True:
        i += k
        line += 1
        if N <= i:
            print(line)
            break
        k += 6
