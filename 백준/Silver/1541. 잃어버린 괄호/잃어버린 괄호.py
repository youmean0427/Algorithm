import sys
input = sys.stdin.readline


input_value = input()
sub = ''
arr = []
for i in input_value:
    if i.isdigit() == False:
        arr.append(int(sub))
        arr.append(i)
        sub = ''
    if i.isdigit():
        sub += i

arr = arr[:-1:]

new = []
p_count = 0
for k in arr:
    if k != '-':
        new.append(k)
    elif k == '-':
        if new and p_count == 1:
            new.append(')')
            p_count = 0
        new.append(k)
        new.append('(')
        p_count = 1

if p_count == 1:
    new.append(')')

total = 0
check = 'plus'

sub = 0
while new:

    x = new.pop()

    if x == ')':
        check = 'minus'
        continue

    if x == '(':
        check = 'plus'
        total -= sub
        sub = 0
        continue

    if check == 'minus' and type(x) == int:
        sub += x

    if check == 'plus' and type(x) == int:
        total += x

print(total)