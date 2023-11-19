function solution(a, b, n) {
    var answer = 0;
    let x = n
    let y = 0
    
    while (x >= a) {
        y = Math.trunc(x / a) * b
        answer += y
        x = y + (x % a) 
    }

    return answer
}