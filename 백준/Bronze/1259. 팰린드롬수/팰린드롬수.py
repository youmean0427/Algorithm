
flag = 1
while flag:
    N = input()
    if N == str(0):
        flag = 0
        break
    if N == N[::-1]:
        print('yes')
    else:
        print('no')
