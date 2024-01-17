import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement as cr

N, M = map(int, input().split())
arr = [int(i) for i in input().split()]
arr.sort()
x = list(cr(arr, M))
x.sort(key= lambda x : x[0])

for i in x:
    print(*i)
