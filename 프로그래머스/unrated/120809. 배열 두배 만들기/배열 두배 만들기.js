function solution(numbers) {
    
    let arr = numbers
    
    for (let i = 0; i < arr.length; i++) {
        arr[i] = arr[i] * 2
    }
    
    var answer = arr;
    return answer;
}