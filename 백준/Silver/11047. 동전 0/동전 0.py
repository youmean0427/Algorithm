import sys
input = sys.stdin.readline

N, K = map(int,(input().split()))
coin = []

for _ in range(N):
    coin.append(int(input()))

count = 0
for i in coin[::-1]:
    if i <= K:
        count += K // i
        K = K % i
print(count)