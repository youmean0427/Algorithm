flag = 1
while flag:

    text = input()
    stack = list()

    if text == '.':
        flag = 0
        break

    for i in text:
        if i == '(' or i == '[':
            stack.append(i)
        if stack and i == ')' and stack[-1] == '(':
            stack.pop()

        elif stack and i == ']' and stack[-1] == '[':
            stack.pop()

        elif i == ')' or i == ']':
            stack.append(i)

    if stack:
        print('no')

    else:
        print('yes')

