from itertools import permutations

def solution(numbers):
    answer = []
    x = set(permutations(numbers, 2))
    
    for i in x:
        answer.append(sum(i))
        
    answer = list(set(answer))
    answer.sort()
    return answer