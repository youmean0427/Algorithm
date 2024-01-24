from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    time = 0
    while truck_weights:
        time += 1
        y = bridge.pop()
        bridge_weight -= y
        if bridge_weight+truck_weights[0] <= weight:
            x = truck_weights.popleft()
            bridge.appendleft(x)
            bridge_weight += x
        else:
            bridge.appendleft(0)
    
    answer = time + bridge_length

    return answer