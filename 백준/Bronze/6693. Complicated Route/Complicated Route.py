import sys
input = sys.stdin.readline

def move(dir, x, y, z):
    d = (2 ** (1 / 2) / 2)

    if (dir == 'N'):
        y += 1 * z
    elif (dir == 'NE'):
        x += d * z
        y += d * z
    elif (dir == 'E'):
        x += 1 * z
    elif (dir == 'SE'):
        x += d * z
        y -= d * z
    elif (dir == 'S'):
        y -= 1 * z
    elif (dir == 'SW'):
        x -= d * z
        y -= d * z
    elif (dir == 'W'):
        x -= 1 * z
    elif (dir == 'NW'):
        x -= d * z
        y += d * z
    return (x, y)

while (1):
    inp = input().split()
    if (inp[0] == "END"):
        break
    arr = inp[0][:len(inp[0])-1].split(",")

    x = 0
    y = 0
    for m in arr:

        dir_arr = ''
        step = ''
        for l in range(len(m)):
            if (m[l] == 'N' or m[l] == 'W' or m[l] == 'S' or m[l] == 'E'):
                dir_arr += m[l]
            else:
                step += m[l]
        x, y = move(dir_arr, x, y, int(step))

    total = ((x - 0) ** 2 + (y - 0) ** 2) ** (1/2)
    print(f"You can go to ({x:.3f},{y:.3f}), the distance is {total:.3f} steps.")

