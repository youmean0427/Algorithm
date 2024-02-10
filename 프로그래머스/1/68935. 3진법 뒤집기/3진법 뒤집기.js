function solution(n) {
    const x = n.toString(3)
    const x_rev = [...x].reverse()
    let answer = x_rev.join("")
    answer = parseInt(answer, 3)
    return answer;
}