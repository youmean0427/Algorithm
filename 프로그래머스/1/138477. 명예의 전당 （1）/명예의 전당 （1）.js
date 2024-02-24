function solution(k, score) {
    var answer = [];
    let arr = []
    score.forEach((x) => {
        arr.push(x)
        arr.sort((a, b) => b - a )
        if (arr.length > k) {
            arr.pop()
        }
        answer.push(arr[arr.length-1])
    })
    return answer;
}