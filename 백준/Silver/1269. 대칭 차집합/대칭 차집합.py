import sys
input = sys.stdin.readline

a_len, b_len = map(int, input().split())

a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())

print(len((a - b) | (b - a)))