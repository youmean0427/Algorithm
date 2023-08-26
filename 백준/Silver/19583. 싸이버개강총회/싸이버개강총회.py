import sys
input = sys.stdin.readline
import datetime

S, E, Q = input().split()
times = []

S = datetime.time(hour=int(S[0:2]), minute=int(S[3:5]))
E = datetime.time(hour=int(E[0:2]), minute=int(E[3:5]))
Q = datetime.time(hour=int(Q[0:2]), minute=int(Q[3:5]))

cnt = 0
names = set()

while True:
    try:
        chat, name = input().split()
        chat_time = datetime.time(hour= int(chat[0:2]), minute=int(chat[3:5]))
        if chat_time <= S:
            names.add(name)
        if E <= chat_time <= Q and name in names:
            names.remove(name)
            cnt += 1
    except:
        break

print(cnt)