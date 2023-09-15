
import sys
input = sys.stdin.readline

T = int(input())


rules = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(T):

    S = list(input().rstrip())
    K = S.copy()
    visited = []
    result = 'Good'

    start = S.pop(0)
    if start in rules:
        visited.append(start)

    while S:
        a = S.pop(0)


        if a == 'A':
            visited.append(a)

        if a == 'F':
            if visited and 'A' in visited:
                visited.append(a)

        if a == 'C':
            if visited and 'F' in visited:
                visited.append(a)

        if a != 'C' and a in rules:
            if visited:
                if visited[-1] == 'C':
                    visited.append(a)


    if 'A' in visited and 'F' in visited and 'C' in visited:
        if K == visited:
            result = 'Infected!'

    print(result)