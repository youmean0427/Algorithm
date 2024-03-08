def solution(genres, plays):
    
    answer = []
    songs = {}
    total = {}
    
    for i in range(len(genres)):
        if genres[i] in songs:
            songs[genres[i]].append((i,plays[i]))
            total[genres[i]] += plays[i]
        else:
            songs[genres[i]] = [(i, plays[i])]
            total[genres[i]] = plays[i]
    
    total_sort = sorted(total.items(), key = lambda x : -x[1])

    for genre, count in total_sort:
        songs_sort = sorted(songs[genre], key = lambda x: -x[1])
        for x, y in songs_sort[:2]:
            answer.append(x)
    
    return answer