import sys

input = sys.stdin.readline
# sys.stdin = open("EX.txt", "r")

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(int(x) for x in input().split())
    print(sum(arr))