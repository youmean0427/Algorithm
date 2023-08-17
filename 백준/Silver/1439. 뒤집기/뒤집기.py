import sys
input = sys.stdin.readline

S = input()

sub = []
oo = []  # 연속된 '0' 리스트
zz = []  # 연속된 '1' 리스트

for i in range(len(S)):

    if i == 0:
        sub.append(S[i])

    elif S[i] == S[i-1]:
        sub.append(S[i])

    elif S[i] != S[i-1]:
        if S[i-1] == '0':
            oo.append(sub)
            sub = list()
            sub.append(S[i])


        elif S[i-1] == '1':
            zz.append(sub)
            sub = list()
            sub.append(S[i])

print(min(len(zz), len(oo)))
