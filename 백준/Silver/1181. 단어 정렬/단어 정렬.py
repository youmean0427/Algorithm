N = int(input())
words = []
for i in range(N):
    words.append(input())

words = set(words)
words = list(words)
words.sort()
words.sort(key=lambda x: len(x))

for i in words:
    print(i)
