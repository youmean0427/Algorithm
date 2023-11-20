function solution(n) {
    var answer = [];
    let i = 1
    while (i <= n) {
        (i % 2 == 0) ? i : answer.push(i)
        i += 1
    }
    return answer;
}