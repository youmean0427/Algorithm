import sys
input = sys.stdin.readline

nums = [int(x) for x in input().split()]
dict = {}
for i in nums:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

dict = sorted(dict.items(), key=lambda x : (-x[1], -x[0]))

if dict[0][1] == 3:
    answer = 10000 + dict[0][0] * 1000
elif dict[0][1] == 2:
    answer = 1000 + dict[0][0] * 100
else:
    answer = dict[0][0] * 100

print(answer)