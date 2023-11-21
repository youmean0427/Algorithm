function solution(s){
    
    let answer = false
    let arr = s.split("")
   
    let i = 0
    let cnt = 0
    
    if (arr[0] == ")") {
        return answer
    }
    
    while (i < arr.length) {
        
        if (arr[i] == "(") {
            cnt += 1
        } else if (cnt >= 1) {
            cnt -= 1
        }
        i += 1
    }
    
    (cnt > 0) ? answer = false : answer = true
    return answer;
}