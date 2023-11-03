function solution(arr) {
    
    const x = arr.reduce((a, b) => a + b, 0)
    const y = arr.length
    
    return x/y;
}