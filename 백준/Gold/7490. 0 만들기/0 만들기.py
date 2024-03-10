import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

def dfs(n, sm, arr):
    global result

    if n >= N+1:
        if sm == 0:
            result.append("".join(arr))
        return

    dfs(n+1, sm+nums[n], arr+["+", str(nums[n])])
    dfs(n+1, sm-nums[n], arr + ["-", str(nums[n])])

    if len(arr) >= 2:
        if arr[-2] == "+":
            dfs(n+1, sm - int(arr[-1]) + int(arr[-1]+str(nums[n])), arr + [" ", str(nums[n])])
        elif arr[-2] == "-":
            dfs(n + 1, sm + int(arr[-1]) - int(arr[-1] + str(nums[n])), arr + [" ", str(nums[n])])
    else:
        dfs(n+1, int(arr[-1] + str(nums[n])), arr + [" ", str(nums[n])])


T = int(input())
for _ in range(T):
    N = int(input())
    nums = [i for i in range(N+1)]
    result = []
    dfs(2, 1, [str(nums[1])])

    result.sort()
    for res in result:
        print(res)
    print()
    
