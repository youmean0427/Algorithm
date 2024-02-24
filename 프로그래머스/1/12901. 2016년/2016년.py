def solution(a, b):
    answer = ''
    last_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6: "WED", 0: "THU"}
    
    data = sum(last_day[:a]) + b
    answer = day[data % 7]

    return answer