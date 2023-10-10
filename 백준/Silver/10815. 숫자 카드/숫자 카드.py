import sys
input = sys.stdin.readline

def binary_search(start, end, card, i):

    while start <= end:

        mid = (start + end) // 2
        if find_cards[mid] == card:
            result[i] = 1
            return

        elif find_cards[mid] < card:
            start = mid + 1

        elif find_cards[mid] > card:
            end = mid - 1

N = int(input())
find_cards = [int(x) for x in input().split()]
find_cards.sort()

M = int(input())
cards = [int(x) for x in input().split()]
result = [0] * M

for i in range(M):
    binary_search(0, N-1, cards[i], i)
print(*result)