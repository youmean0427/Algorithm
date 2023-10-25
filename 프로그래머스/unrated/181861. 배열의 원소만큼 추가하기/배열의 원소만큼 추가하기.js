function solution(arr) {
    var answer = [];
    
    for (i in arr) {
        for (let j = 0; j < arr[i]; j++) {
            answer.push(arr[i])
        }
    }
    
    
    return answer;
}