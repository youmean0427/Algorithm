function solution(genres, plays) {
    
    let songs = {}
    let total = {}
    var answer = [];
    
    for (let i = 0; i < genres.length; i++) {
        if (genres[i] in songs) {
            songs[genres[i]].push([i, plays[i]])
            total[genres[i]] += plays[i]
        } else {
            songs[genres[i]] = [[i, plays[i]]]
            total[genres[i]] = plays[i]
        }
    }
    
    const total_sort = Object.entries(total).sort((a, b) => b[1] - a[1])
    total_sort.forEach(x => {
       songs[x[0]].sort((a, b) => b[1] - a[1]).slice(0, 2).map(x => {answer.push(x[0])} )
    })
    
    return answer;
}