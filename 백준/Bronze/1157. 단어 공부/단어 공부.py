char = input()

char2 = char.lower()
char = char.lower()
char = set(char)
char = list(char)

num = 0
for i in char:
    char_cnt = char2.count(i)
    if num == char_cnt:
        result = '?'
    if num < char_cnt:
        num = char_cnt
        result = i

print(result.upper())