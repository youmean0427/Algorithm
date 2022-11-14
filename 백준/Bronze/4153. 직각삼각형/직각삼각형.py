while 1:
    a = list(map(int, input().split()))
    a.sort()

    if a[0] == 0:
        break
    if a[2]*a[2] == a[1]*a[1] + a[0]*a[0]:
           print("right")
    else:
            print("wrong")


