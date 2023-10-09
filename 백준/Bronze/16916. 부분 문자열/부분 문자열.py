import sys
input = sys.stdin.readline

def kmp_table(pattern):

    p = len(pattern)
    F = [0] * p

    i = 1
    j = 0

    while i < p:

        if pattern[i] == pattern[j]:
            F[i] += j + 1
            i += 1
            j += 1

        elif j > 0:
            j = F[j-1]

        else:
            i += 1

    return F

def kmp (pattern, text):

    p = len(pattern)
    t = len(text)

    F = kmp_table(pattern)

    i = 0  # text
    j = 0  # pattern

    while i < t:

        if text[i] == pattern[j]:
            if j == p - 1:
                return 1
            i += 1
            j += 1

        elif j > 0:
            j = F[j-1]

        else:
            i += 1

    return 0

text = input().rstrip()
pattern = input().rstrip()


print(kmp(pattern, text))