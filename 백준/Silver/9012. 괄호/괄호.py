import sys
input=sys.stdin.readline

T = int(input())
for _ in range (T):
    ps = input()
    arr = list()
    for i in ps:
        arr.append(i)

    result = list()
    arr = arr[:len(arr)-1]

    while arr:
        test = arr.pop(0)
        if result and result[len(result)-1] == '(' and test == ')':
            result.pop(-1)
        else:
            result.append(test)

    if result:
        print('NO')
    else:
        print('YES')