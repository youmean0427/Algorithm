def skip_table(pattern):

    skip = [len(pattern)] * 256

    for i in range(len(pattern)):
        skip[ord(pattern[i])] = len(pattern) - i - 1
    return skip

def boyer_moore(pattern, text):

    p = len(pattern)
    t = len(text)

    skip = skip_table(pattern)

    i = p - 1

    while i < t:
        j = p - 1
        while text[i] == pattern[j]:
            if j == 0:
                return 1

            i -= 1
            j -= 1

        if skip[ord(text[i])] > p - j :
            i += skip[ord(text[i])]
        else:
            i += p - j

    return 0

def solution(myString, pat):
    myString = myString.upper()
    pat = pat.upper()
    answer = boyer_moore(pat, myString)
        
    return answer
