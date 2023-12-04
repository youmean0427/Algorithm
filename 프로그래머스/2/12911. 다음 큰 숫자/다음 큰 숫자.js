function solution(n) {
    var answer = 0;
    
    function change(n) {
        const x = n.toString(2)
        const arr = [...x]
        const cnt = arr.filter(x => x == 1)
    return cnt.length
    }
    
    const n_cnt = change(n)
    
    let i = n+1
    while (i) {
        if (n_cnt === change(i)){
            answer = i
            break
        }
        i++
    }
    
    return answer;
}
