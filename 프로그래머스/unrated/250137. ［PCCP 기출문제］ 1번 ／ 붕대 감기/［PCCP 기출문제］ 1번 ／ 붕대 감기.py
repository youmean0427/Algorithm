def game(bandage,health,attacks):
    end_time = attacks[-1][0] 
    now = 1
    x = attacks.pop(0)
    hp = health
    cnt = 0
    while now <= end_time:

        if x[0] == now:
            hp -= x[1]
            cnt = 1
            if attacks:
                x = attacks.pop(0)
            if hp <= 0:
                return -1
    
        elif cnt == bandage[0]:
            cnt = 1
            hp += bandage[1] + bandage[2]
            if hp > health:
                hp = health

        else:
            hp += bandage[1]
            if hp > health:
                hp = health
            cnt += 1

        now += 1
    return hp


def solution(bandage, health, attacks):
    answer = 0
    answer = game(bandage,health,attacks)

    return answer