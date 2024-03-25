function solution(ingredient) {
    var answer = 0;
    let stack = []
    let idx = 0
    
    for (let i = 0; i < ingredient.length; i++) {
        stack.push(ingredient[i])
        idx += 1
        if (idx >= 4) {
            if (stack.slice(idx-4, idx).join("") == 1231) {
                let cnt = 0
                answer += 1
                while (cnt < 4){
                    stack.pop()
                    cnt += 1
                }
                idx = stack.length
            }
        } 
    }
    return answer;
}