import sys
input = sys.stdin.readline

def KMP_table(pattern):
    F = [0] * len(pattern)
    i = 1
    j = 0

    while i < len(pattern):

        if pattern[j] == pattern[i]:
            F[i] += j+1
            i += 1
            j += 1
        elif j > 0:
            j = F[j-1]

        else:
            i += 1

    return F


def KMP (text, pattern):

    t = len(text)
    p = len(pattern)
    F = KMP_table(pattern)

    i = 0
    j = 0
    result = []
    while (i < t):

        if text[i] == pattern[j]:
            if j == p - 1:
                result.append(i-j+1)
                i += 1
                j = F[j]
            else:
                i += 1
                j += 1

        else:
            if j > 0:
                j = F[j-1]
            else:
                i += 1

    return result

text = input().rstrip()
pattern = input().rstrip()
result = (KMP(text, pattern))

print(len(result))
print(*result)