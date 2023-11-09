function solution(strings, n) {
    var answer = [];
    
    var info = []
    
    for (let i = 0; i < strings.length; i++) {
        info.push([strings[i][n], strings[i], i])
    }
 
    info.sort((a, b) => {
        if (a[0] == b[0]) {
            if (a[1] > b[1]) {
            return 1
            } else {
                return -1
            }
        } else if (a[0] > b[0]) {
            return 1            
        } else {
            return -1
        }
    })
    
    for (let i = 0; i < info.length; i++) {
        answer.push(info[i][1])
    }
    
    return answer;
}