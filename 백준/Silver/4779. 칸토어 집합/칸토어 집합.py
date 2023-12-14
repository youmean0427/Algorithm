def cantor(x, start, end):
    if start < end:
        mid = (end - start + 1) // 3
        for i in range(start + mid, start + 2 * mid):
            x[i] = " "
        cantor(x, start, start + mid - 1)
        cantor(x, start + 2 * mid, end)

while True:
    try:
        N = int(input())
        arr = ['-'] * (3 ** N)
        cantor(arr, 0, len(arr) - 1)
        print("".join(arr))

    except EOFError:
        break