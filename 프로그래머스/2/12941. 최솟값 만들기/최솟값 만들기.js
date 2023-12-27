function solution(A,B){
    var answer = 0;
    let arr = []
    
    A.sort((a, b) => a - b)
    B.sort((a, b) => b - a)
   
    arr = A.map((x, idx) => x * B[idx])
    answer = arr.reduce((a, b) => a + b, 0)
    
    return answer;
}