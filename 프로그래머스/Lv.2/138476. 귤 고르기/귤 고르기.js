function solution(k, tangerine) {
    let answer = 0;
    
    let cnt = {}
    
    for (let i of tangerine) {
        i in cnt ? cnt[i] += 1 : cnt[i] = 1
    }
    // 1. for
    // 2. Object.entries
    
    let sortCnt = Object.entries(cnt)
    sortCnt.sort((a, b) => b[1] - a[1])
    
    let total = []
    while (k > 0) {
        let line = sortCnt.shift()
        k -= line[1]
        total.push(line[0])
    }
    
    answer = total.length
    return answer;
}