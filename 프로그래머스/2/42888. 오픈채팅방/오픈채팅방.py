def solution(record):
    answer = []
    arr = []
    id = {}
    
    for i in record:
        line = i.split(' ')
        if line[0] == "Enter":
            arr.append((line[1], line[0]))
            id[line[1]] = line[2]
        elif line[0] == "Leave":
            arr.append((line[1], line[0]))
        else:
            id[line[1]] = line[2]
    
    for i in arr:
        if i[1] == "Enter":
            answer.append(f'{id[i[0]]}님이 들어왔습니다.')
        elif i[1] == "Leave":
            answer.append(f'{id[i[0]]}님이 나갔습니다.')
    

    return answer