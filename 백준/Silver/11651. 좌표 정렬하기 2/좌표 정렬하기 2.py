import sys
input=sys.stdin.readline

T = int(input())
box = list()

for i in range (T):
    a, b = map(int, input().split())
    box.append((a, b))

key = lambda x : (x[1], x[0])
result = sorted(box, key = key)
for k in result:
    print(k[0], k[1])