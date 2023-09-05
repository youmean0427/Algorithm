import sys
input = sys.stdin.readline

S = input()
result = ''
for i in S:
    if i.islower():
        A = i.upper()
        result += A
    else:
        A = i.lower()
        result += A

print(result)

