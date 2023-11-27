import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
S = deque([])
T = ""
for _ in range(N):
    S.append(input().rstrip())

while S:
    x = S[0]
    y = S[-1]

    if ord(x) < ord(y):
        T += S.popleft()
    elif ord(x) > ord(y):
        T += S.pop()
    else:
        if len(S) >= 4:
            i = 1
            j = -2
            while True:

                if ord(S[i]) < ord(S[j]):
                    T += S.popleft()
                    break
                elif ord(S[i]) > ord(S[j]):
                    T += S.pop()
                    break
                elif len(S) % 2 != 0 and len(S) // 2 == i:
                    T += S.popleft()
                    break
                elif len(S) % 2 == 0 and len(S) // 2 == i+1:
                    T += S.popleft()
                    break
                else:
                    i += 1
                    j -= 1
        else:
            T += S.popleft()

cnt = 0
while cnt < len(T):
    print(T[cnt:cnt+80])
    cnt += 80