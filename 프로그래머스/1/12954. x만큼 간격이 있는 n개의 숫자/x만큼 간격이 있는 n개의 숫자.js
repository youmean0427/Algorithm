function solution(x, n) {
    var answer = [];
    if (x > 0) {
        for (let i = x; i <= x * n; i += x) {
            answer.push(i)
        }
    } else if(x < 0) {
        for (let i = x; i >= x * n; i += x) {
            answer.push(i)
        }
    } else {
        for (let i = x; i < n; i++) {
            answer.push(x)
        }
    }
    
    
    return answer;
}