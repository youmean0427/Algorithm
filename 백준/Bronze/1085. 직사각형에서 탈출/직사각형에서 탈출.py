x, y, w, h = map(int, input().split())
result = 1000

if x - 0 <= result:
    result = x - 0
if y - 0 <= result:
    result = y - 0
if w - x <= result:
    result = w - x
if h - y <= result:
    result = h - y
print(result)