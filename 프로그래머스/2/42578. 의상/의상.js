function solution(clothes) {
    var answer = 1;
    var cnt = {}

    
    clothes.forEach(x =>{
        if (x[1] in cnt) {
            cnt[x[1]] += 1
        } else {
            cnt[x[1]] = 1
        }
    })

    const cntValue = Object.values(cnt)
    cntValue.forEach(x => answer *= (x+1))
    answer -= 1
    return answer;
}