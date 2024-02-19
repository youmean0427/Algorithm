function solution(n, m, section) {
    var answer = 0;
    let arr = new Array(n+m).fill(1)
    
    for (let i of section) {
        arr[i] = 0
    }
    
    let idx = 1
    while (idx <= n) {
        if (arr[idx] == 0) {
            for (let i = idx; i < idx+m; i++) {
                arr[i] = 1
            }
            answer += 1
            idx += m
        }
        else {
            idx += 1
        }
    }
    return answer;
}