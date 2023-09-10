import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

player = [y for y in range(N)]
player_case = list(combinations(player, N//2))
cnt = len(player_case) // 2

result = []

for i in range(cnt):

    start = player_case[i]
    start_score = 0
    for j in range(len(start)):
        for k in range(j+1, len(start)):
            start_score += arr[start[j]][start[k]]
            start_score += arr[start[k]][start[j]]

    link = player_case[-(i+1)]
    link_score = 0
    for j in range(len(link)):
        for k in range(j + 1, len(link)):
            link_score += arr[link[j]][link[k]]
            link_score += arr[link[k]][link[j]]

    result.append(abs(start_score-link_score))

print(min(result))
