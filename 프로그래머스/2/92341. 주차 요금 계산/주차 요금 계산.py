from datetime import datetime
import math
def solution(fees, records):
    answer = []
    parking = {}
    parking_time = {}
    
    def time_diff(start, end):
        end = end.split(":")
        start = start.split(":")
        minute = int(end[1]) - int(start[1])
        hour = int(end[0]) - int(start[0])
        
        time1 = datetime(2024, 1, 1, int(start[0]), int(start[1]))
        time2 = datetime(2024, 1, 1, int(end[0]), int(end[1]))
        diff = time2 - time1
        return diff.total_seconds() // 60

    def cost(minute):
        if fees[0] >= minute:
            return fees[1]
        return fees[1] + math.ceil((minute - fees[0]) / fees[2]) * fees[3]
        
    for i in records:
        line = i.split(" ")

        if line[2] == 'IN':
            parking[line[1]] = line[0]
        elif line[2] == 'OUT':
            if line[1] in parking:
                if line[1] in parking_time:
                    parking_time[line[1]] += time_diff(parking[line[1]], line[0])
                else:
                    parking_time[line[1]] = time_diff(parking[line[1]], line[0])
                
                del parking[line[1]]

    for i in parking:
        if i in parking_time:
            parking_time[i] += time_diff(parking[i], '23:59')
        else:
            parking_time[i] = time_diff(parking[i], '23:59')
            
    parking_time = sorted(parking_time.items(), key=lambda x: x[0])

    for i in parking_time:
        answer.append(cost(i[1]))
        
    return answer