num = []
for _ in range(10):
    num.append(int(input()))

result = []
for i in num:
    result.append(i%42)
    
print(len(set(result)))