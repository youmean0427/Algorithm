N = int(input())

for i in range(N):
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    arrA = arrA[1:]
    arrB = arrB[1:]

    if arrA.count(4) > arrB.count(4):
        print('A')
    elif arrA.count(4) < arrB.count(4):
        print('B')
    elif arrA.count(4) == arrB.count(4):
        if arrA.count(3) > arrB.count(3):
            print('A')
        elif arrA.count(3) < arrB.count(3):
            print('B')
        elif arrA.count(3) == arrB.count(3):
            if arrA.count(2) > arrB.count(2):
                print('A')
            elif arrA.count(2) < arrB.count(2):
                print('B')
            elif arrA.count(2) == arrB.count(2):
                if arrA.count(1) > arrB.count(1):
                    print('A')
                elif arrA.count(1) < arrB.count(1):
                    print('B')
                elif arrA.count(1) == arrB.count(1):
                    print('D')
