def solution(storey):
    answer = 0
    arr = list(map(int, list(str(storey))))[::-1]
    arr.append(0)
    
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
            
        if arr[i] == 5:
            answer += 5
            if arr[i+1]+1 > 5:
                arr[i+1] += 1
        elif arr[i] > 5:
            answer += 10 - arr[i]
            arr[i+1] += 1
        elif arr[i] < 5:
            answer += arr[i]

    return answer