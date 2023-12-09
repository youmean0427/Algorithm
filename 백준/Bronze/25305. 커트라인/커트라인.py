import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(x) for x in input().split()]
arr.sort(reverse=True)
print(arr[:K][-1])