import sys, math
input = sys.stdin.readline

L = int(input())
arr = [int(i) for i in input().split()]

arr.sort()
print(arr[0]*arr[-1])