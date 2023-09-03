import sys
input = sys.stdin.readline

def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

T = int(input())
for _ in range(T):
    total = 0
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)-1):
        for j in range(i+1, len(nums)):
            total += GCD(nums[i], nums[j])
    print(total)