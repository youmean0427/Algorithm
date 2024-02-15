import sys
input = sys.stdin.readline

S = input().rstrip()
q = list(S)

max_box = []
min_box = []

max_ans = ''
min_ans = ''

while q:
    x = q.pop(0)

    if x == 'M':
        max_box.append(x)
        min_box.append(x)

    if x == 'K':
        max_box.append(x)

        if max_box:
            max_ans += '5' + (len(max_box)-1) * '0'
            max_box.clear()
        else:
            max_ans += '5'

        if min_box:
            min_ans += '1' + (len(min_box)-1) * '0'
            min_box.clear()
            min_ans += '5'
        else:
            min_ans += '5'

if max_box:
    max_ans += (len(max_box)) * '1'
if min_box:
    min_ans += '1' + (len(min_box) - 1) * '0'

print(max_ans)
print(min_ans)