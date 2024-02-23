def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for i in range(len(cities)):
        cities[i] = cities[i].upper()

    for i in cities:
        if i in cache:
            answer += 1
            cache.pop(cache.index(i))
            cache.append(i)
            continue
        
        if len(cache) < cacheSize:
            cache.append(i)
            answer += 5
        elif cache:
            cache.pop(0)
            cache.append(i)
            answer += 5
    
    if cacheSize == 0:
        answer = len(cities) * 5
    
    return answer