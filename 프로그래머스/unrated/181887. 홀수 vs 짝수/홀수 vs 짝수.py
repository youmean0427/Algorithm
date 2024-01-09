def solution(num_list):
    odd = 0
    even = 0
    for i in range(0, len(num_list)):
        if i % 2 == 0:
            odd += num_list[i]
        else:
            even += num_list[i]
    
    answer = max(odd, even)
    return answer