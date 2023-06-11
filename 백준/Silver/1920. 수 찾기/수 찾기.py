import sys
input=sys.stdin.readline

N = int(input())
Aarr = list(map(int, input().split()))

M = int(input())
Barr = list(map(int, input().split()))

Aarr = set(Aarr)
Barr2 = set(Barr)

E = Aarr & Barr2

for i in Barr:
    if i in E:
        print(1)
    else:
        print(0)