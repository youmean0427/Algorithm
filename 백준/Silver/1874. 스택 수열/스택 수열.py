from collections import deque

T = int(input())

arr = deque()
for _ in range(T):
    num = int(input())
    arr.append(num)

# print(arr)

stack = deque()
result = deque()

count = 1

while arr:

    if count > T+1:
        break

    if stack and stack[-1] == arr[0]:
        stack.pop()
        arr.popleft()
        result.append('-')

    else:
        stack.append(count)
        count += 1
        result.append('+')

if count > T+1:
    print("NO")
else:
    for i in result:
        print(i)