import sys
input = sys.stdin.readline

N = int(input())
find_cards = [int(x) for x in input().split()]
M = int(input())
cards = [int(x) for x in input().split()]

sorted_cards = []
for i in range(M):
    sorted_cards.append((cards[i], i))
sorted_cards.sort()
result = [0] * M

for i in find_cards:

    start = 0
    end = M-1
    flag = 1
    while start <= end and flag:

        mid = (start + end) // 2
        if sorted_cards[mid][0] == i:
            result[sorted_cards[mid][1]] = 1
            flag = 0

        elif sorted_cards[mid][0] < i:
            start = mid + 1

        elif sorted_cards[mid][0] > i:
            end = mid - 1

print(*result)
