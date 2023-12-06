import sys
input = sys.stdin.readline

N = int(input())
answer = "long int"

i = N // 4
while i > 1:
    answer = "long " + answer
    i -= 1

print(answer)