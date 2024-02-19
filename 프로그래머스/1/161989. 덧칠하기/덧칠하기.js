function solution(n, m, section) {
    var answer = 0;
    let painted = 0;
    
    for (let i of section) {
        if (painted < i) {
            answer += 1
            painted = i + m - 1
        }
    }
    
    return answer;
}