function solution(s)
{
    var answer = 1;
    var arr = s
    const start= s[0]
    let stack = [start]
    
    let i = 1
    while (i < arr.length) {
        const x = arr[i]
        if (stack[stack.length-1] === x) {
            stack.pop()
            i += 1
        } else {
            stack.push(x)
            i += 1
        }
    }
    
    if (stack.length) {
        answer = 0
    }
    
    return answer;
}