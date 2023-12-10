import sys, math
input = sys.stdin.readline


def check(x):
    while True:
        cnt = 0
        if x < 2:
            x += 1
            continue
        for i in range(2, int(x ** (1/2))+1):
            if x % i == 0:
                cnt = 1
                break
        if cnt == 0:
            return x
        x += 1
        
T = int(input())
for _ in range(T):
    x = int(input())
    answer = check(x)
    print(answer)