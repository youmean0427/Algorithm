import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

# 4분면
# 0 1
# 2 3

num = 0

while N != 0:
    N = N-1
    size = 2 ** N
    if 0 <= r < size and 0 <= c < size:          # 0사분면
        num += (2**N) * (2**N) * 0
    if r < size and c >= size :                  # 1사분면
        num += (2**N) * (2**N) * 1
        c -= size
    if r >= size and c < size:                   # 2사분면
        num += (2**N) * (2**N) * 2
        r -= size
    if r >= size and c >= size:                  # 3사분면
        num += (2**N) * (2**N) * 3
        c -= size
        r -= size
print(num)