import sys
input = sys.stdin.readline

T = int(input())

def fibo (n):
    table = [0, 1]

    for i in range(2, n+1):
        table.append(table[i-1] + table[i-2])

    return (table[n-1], table[n])

for _ in range(T):
    N = int(input())
    result = fibo(N)
    print(result[0], result[1])