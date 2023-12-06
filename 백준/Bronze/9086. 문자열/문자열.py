import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    answer = S[0] + S[-1]
    print(answer)