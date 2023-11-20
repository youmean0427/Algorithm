function solution(array) {
    var answer = 0;
    let i = array.length / 2
    i = Math.trunc(i)
    
    array.sort((a, b) => a - b)
    
    answer = array[i]
    return answer;
}