function solution(s) {
    var answer = [];

    let zero = 0
    let cnt = 0
    
    while (s.length > 1) {
        let ch = ''
        let zeroCnt = 0
        for (let i = 0; i < s.length; i++) {
            if (s[i] == '1') {
                ch += '1'
            } else {
                zeroCnt += 1 
            }
        }
        zero += zeroCnt
        let len = (s.length - zeroCnt).toString(2)
        s = len
        cnt += 1
    }
    
    answer = [cnt, zero]
    return answer;
}