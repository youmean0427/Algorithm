def rabin_karf (pattern, text, N):

    pattern = pattern.upper()
    text = text.upper()

    hash_p = 0
    hash_t = 0

    p = len(pattern)
    t = len(text)

    if p > t:
        return 0

    for i in range(p):
        hash_p += ord(pattern[i]) * N ** (p-i-1)
        hash_t += ord(text[i]) * N ** (p-i-1)


    for i in range(t-p+1):
        if hash_p == hash_t:
            return 1

        if i < t-p:
            hash_t = ((hash_t-(ord(text[i]) * N ** (p-1))) * N + ord(text[i+p])) * 1


    return 0


def solution(text, pattern):
    N = 31
    answer = rabin_karf(pattern, text, N)
    return answer
