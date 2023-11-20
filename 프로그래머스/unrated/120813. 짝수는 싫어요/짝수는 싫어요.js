function solution(n) {
    var answer = [];
    let i = 1
    let j = 0
    while (i <= n) {
        (i % 2 == 0) ? j = 1 : answer.push(i)
        i += 1
    }
    
    return answer;
}