def solution(survey, choices):
    answer = ''
    alpha = ["R", "T", "C", "F", "J", "M", "A", "N"]
    index = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    agree = {1 : 3, 2: 2, 3: 1}
    
    N = len(survey)
    for i in range(N):
        if choices[i] < 4:
            index[survey[i][0]] +=  agree[choices[i]] 
        elif choices[i] > 4:
            index[survey[i][1]] += choices[i] - 4
            

    for i in range(0, len(alpha), 2):
        if index[alpha[i]] >= index[alpha[i+1]]:
            answer += alpha[i]
        else:
            answer += alpha[i+1]
    
    return answer