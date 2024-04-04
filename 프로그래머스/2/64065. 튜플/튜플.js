function solution(s) {
    var answer = [];
    
    s = s.split("},{")
    const n = s.length
    s[0] = s[0].replace(/^\{+|\}+$/g, '')
    s[n-1] = s[n-1].replace(/^\{+|\}+$/g, '')
    
    s.forEach((x, i) => {
        s[i] = x.split(",")
    })
    
    s.sort((a, b) => {
        if (a.length > b.length) {
            return 1
        } else {
            return -1
        }
    })
    
    const cnt = {}
    s[n-1].forEach(x => {
        if (x in cnt) {
            cnt[x] += 1
        } else {
            cnt[x] = 1
        }
    })

    for (let a = 0; a < n; a++) {
        for (let b = 0; b< s[a].length; b++) {
            if (cnt[s[a][b]]) {
                cnt[s[a][b]] -= 1
                answer.push(parseInt(s[a][b]))
            }        
        }
    }
    return answer;
}