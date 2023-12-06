import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())
hh, mm = A, B+C

if B + C >= 60:
    mm = (B + C) % 60
    hh += (B + C) // 60

if hh >= 24:
    hh = hh % 24

print(hh, mm)