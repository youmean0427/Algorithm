from itertools import permutations

def solution(numbers):
    answer = []
    x = set(permutations(numbers, 2))
    
    for i in x:
        if sum(i) in answer:
            continue
        else:
            answer.append(sum(i))
        
    answer.sort()
    return answer