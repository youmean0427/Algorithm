import sys
input = sys.stdin.readline

N = int(input())
pat = [str(x) for x in (input().rstrip().split('*'))]
for _ in range(N):
    arr = [str(x) for x in input().rstrip()]
    pat_0 = [str(x) for x in pat[0]]
    pat_1 = [str(x) for x in pat[1]]
    if pat_0 == arr[:len(pat[0])] and pat_1 == arr[-len(pat[1]):] and len(arr) >= len(pat_0) + len(pat_1):
        print("DA")
    else:
        print("NE")