def solution(dirs):
    global answer
    
    arr = [[0 for _ in range(11)] for _ in range(11)]
    dir = list(dirs)
    
    dir_dict = {"U" : [-1, 0], "D" : [1, 0], "R" : [0, 1], "L" : [0, -1]}
    answer = 0
    
    def dfs(sn, sm):
        global answer
        
        road = []
        stack = [(sn, sm, 0)]
        
        while stack:
            x, y, z = stack.pop()

            if z >= len(dir):
                return road
            
            n, m = dir_dict[dir[z]]
            xn, ym = x + n, y + m
            z += 1

            if 0 <= xn < 11 and 0 <= ym < 11:
                stack.append((xn, ym, z))
                if [(x, y), (xn, ym)] in road or [(xn, ym), (x, y)] in road:
                    continue
                else:
                    road.append([(x, y), (xn, ym)])
            else:
                stack.append((x, y, z))
    
    x = dfs(5, 5)
    answer = len(x)
    return answer