function solution(n) {
    var arr = [0, 1, 1, 2, 3, 5]
    for (let i = 6; i <= n; i++) {
        arr.push(arr[i-1]%1234567 + arr[i-2]%1234567)
    }
    return arr[n]%1234567
}

