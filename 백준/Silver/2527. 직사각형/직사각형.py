import sys
input = sys.stdin.readline

def find(fir, sec):
    x, y, p, q = fir
    xx, yy, pp, qq = sec
    
    # d
    if (xx > p and pp > p):
        print("d")
    elif (yy > q and qq > q):
        print("d")
    elif (qq < y and yy < y):
        print("d")
    elif (pp < x and xx < x):
        print("d")
    # c
    elif (xx == p and yy == q):
        print("c")
    elif (x == pp and y == qq):
        print("c")
    elif (xx == p and y == qq):
        print("c")
    elif (x == pp and yy == q):
        print("c")
    # b
    elif (q - yy == q - y + qq - yy and pp -  x < pp - xx + p - x):
        print("b")
    elif (pp -  x == pp - xx + p - x and qq - y < qq - yy + q - y):
        print("b")
    elif (qq - y == qq - yy + q - y and p - xx < p - x + pp - xx):
        print("b")
    elif (p - xx == p - x + pp - xx and q - yy < q - y + qq - yy):
        print("b")
    # a
    else:
        print("a")
    return

def square(arr):

    idx = 0
    first_square = []
    second_square = []
    while (idx < 8):
        if (idx < 4):
            first_square.append(arr[idx])
        else:
            second_square.append(arr[idx])
        idx += 1

    find(first_square, second_square)

for _ in range(4):
    arr = list(map(int, input().split()))
    square(arr)