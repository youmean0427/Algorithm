import sys
input = sys.stdin.readline

S = input().rstrip()

for i in range(0, len(S), 10):
    print(S[i:i+10])