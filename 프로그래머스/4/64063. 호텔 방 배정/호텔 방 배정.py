import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    def find_empty_room(room, rooms):
        if room not in rooms:
            rooms[room] = room + 1
            return room
        empty = find_empty_room(rooms[room], rooms)
        rooms[room] = empty + 1
        return empty

    rooms = {}
    answer = []
    for room in room_number:
        empty_room = find_empty_room(room, rooms)
        answer.append(empty_room)

    return answer