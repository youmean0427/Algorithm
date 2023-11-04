function solution(absolutes, signs) {
    const answer = signs.reduce((a, b, i) => a + (absolutes[i] * (b ? 1 : -1)), 0)
    return answer;
}