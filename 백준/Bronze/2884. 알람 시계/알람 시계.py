h, m = map(int, input().split())

mm = m - 45

if mm < 0:
    h -= 1
    if h < 0:
        h += 24
    m = 60 + mm

elif mm > 0:
    m = m - 45

elif mm == 0:
    m -= 45

elif h < 0:
    h += 24

print(h, m)