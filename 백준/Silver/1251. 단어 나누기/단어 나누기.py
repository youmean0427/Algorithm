import sys
input = sys.stdin.readline

s = input().rstrip()
s = list(s)
answer = []
for i in range(1, len(s)):
    for j in range(i+1, len(s)):
        a = s[:i]
        b = s[i:j]
        c = s[j:]

        a.reverse()
        b.reverse()
        c.reverse()

        answer.append("".join(a+b+c))

answer.sort()
print(answer[0])
