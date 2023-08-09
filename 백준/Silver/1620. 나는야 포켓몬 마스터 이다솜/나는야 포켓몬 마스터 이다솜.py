from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

monster = {}
number = {}
for i in range(1, N+1):
    name = input().rstrip()
    monster[i] = name
    number[name] = i

for _ in range(M):
    find = input()
    try:
        a = int(find)
        print(monster[a])
    except:
        b = find.rstrip()
        print(number[b])