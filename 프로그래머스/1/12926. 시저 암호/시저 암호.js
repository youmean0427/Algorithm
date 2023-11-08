function solution(s, n) {
    var answer = [] 
   
    for (let i of s) {
        if (i !== " ") {
            let x = i.charCodeAt(0)
            
            if (x <= 90) {
                x += n
                if (x > 90) {
                    x -= 26
                }
            }
            else {
                x += n
                if (x > 122) {
                    x -= 26
                }
            }
            answer.push(String.fromCodePoint(x))
        } else {
            answer.push(i)
        }
    }
    
    return answer.join("")
}

    
