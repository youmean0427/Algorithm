import sys

# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
# 격자
arr = [[[] for _ in range(N)] for _ in range(N)]
# 파이어볼 좌표
fire_pos = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    # m : 질량, s : 속력, d : 방향
    arr[r - 1][c - 1].append((m, s, d))
    fire_pos.append((r - 1, c - 1))

# 8개 방향
dir = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}

add_pos = {}


# 격자 arr를 넣어서, 파이어볼 이동한 새로운 배열 반환
def fireball_move(fm_arr):  # arr
    moved_arr = [[[] for _ in range(N)] for _ in range(N)]
    while fire_pos:
        x, y = fire_pos.pop()
        while fm_arr[x][y]:
            mm, ms, md = fm_arr[x][y].pop()  # 질량, 속력, 방향

            # 이동할 좌표
            dx, dy = dir[md]

            next_x = (dx * ms + x) % N
            next_y = (dy * ms + y) % N

            moved_arr[next_x][next_y] += [(mm, ms, md)]

            if len(moved_arr[next_x][next_y]) >= 2:
                add_pos[(next_x, next_y)] = 1

    return moved_arr


def odd_even(total_d):
    start = total_d[0]
    for i in total_d:
        if start != i:
            return [1, 3, 5, 7]
    return [0, 2, 4, 6]


def fireball_add(fa_arr):
    # add_pos에 2개 이상의 파이어볼 좌표가 저장

    for ax, ay in add_pos:
        if add_pos[(ax, ay)] == 1:
            add_pos[(ax, ay)] = 0
            total_m = 0
            total_s = 0
            total_d = []
            total_cnt = len(fa_arr[ax][ay])
            while fa_arr[ax][ay]:
                fam, fas, fad = fa_arr[ax][ay].pop()

                total_m += fam
                total_s += fas

                if fad % 2 == 0:  # 짝수
                    total_d.append(2)
                else:  # 홀수
                    total_d.append(1)

            if total_m == 0:
                continue

            total_d = odd_even(total_d)
            total_m = total_m // 5
            total_s = total_s // total_cnt

            if total_m == 0:
                continue

            for idx in total_d:
                dx, dy = dir[idx]

                fa_arr[ax][ay].append((total_m, total_s, idx))
            fire_pos.append((ax, ay))
    return fa_arr


def add_result_check(adr_arr):
    for n in range(N):
        for m in range(N):
            if len(adr_arr[n][m]) < 2:
                fire_pos.append((n, m))


idx = 0
while idx < K:
    move_arr = fireball_move(arr)
    arr = fireball_add(move_arr)
    add_result_check(arr)
    idx += 1

ans = 0
for n in range(N):
    for m in range(N):
        for l in range(len(arr[n][m])):
            ans += arr[n][m][l][0]
print(ans)