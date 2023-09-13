import sys
input = sys.stdin.readline
from itertools import combinations, permutations

N = int(input())
K = int(input())

cards = []
for _ in range(N):
    num = int(input())
    cards.append(num)

select_cards = list(combinations(cards, K))
result = set()
for i in select_cards:
    array_cards = list(permutations(i, K))
    for j in array_cards:
        array_num = ''
        for k in j:
            array_num += str(k)
        result.add(int(array_num))

print(len(result))