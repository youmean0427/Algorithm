import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

S = input().strip()

def java_to_c(arr):

    result = []
    start = 0
    for i in range(len(arr)+1):
        if i == 0:
            if arr[i].isupper():
                return "Error!"
        else:
            if i == len(arr):
                result.append("".join(arr[start:len(arr)]).lower())
            elif arr[i].isupper():
                result.append("".join(arr[start:i]).lower())
                start = i

    return "_".join(result)

def c_to_java(arr):

    if "__" in arr:
        return "Error!"
    elif arr[0] == "_" or arr[len(arr)-1] == "_":
        return  "Error!"

    for i in range(len(arr)):
        if arr[i].isupper():
            return "Error!"

    result = arr.split("_")
    ans = []
    for i in range(len(result)):
        if i != 0:
            x = result[i][0].upper()+result[i][1:]
            ans.append(x)
        else:
            ans.append(result[i])

    return "".join(ans)

if "_" in S:
    cj = c_to_java(S)
    print(cj)
else:
    jc = java_to_c(S)
    print(jc)