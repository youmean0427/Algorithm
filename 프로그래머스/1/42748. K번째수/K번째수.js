function solution(array, commands) {
    var answer = [];
    
    for (let x of commands) {
        const result = array.slice(x[0]-1, x[1])
        const sortResult = sort(result)
        answer.push(sortResult[x[2]-1])
    }
    return answer;
}

function sort(arr){
    arr.sort((a, b) => a - b)
    return arr
    
}