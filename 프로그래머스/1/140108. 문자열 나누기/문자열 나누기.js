function solution(s) {
    var answer = 1;
    let char = s[0]
    let charCnt = 1
    let otherCnt = 0
    
    for (let i = 1; i < s.length; i++) {

        if (charCnt === otherCnt) {
            char = s[i]
            charCnt = 1
            otherCnt = 0
            answer += 1
        }
        else if (char === s[i]) {
            charCnt += 1
        } else {
            otherCnt += 1
        }
    }
    
    
    return answer;
}