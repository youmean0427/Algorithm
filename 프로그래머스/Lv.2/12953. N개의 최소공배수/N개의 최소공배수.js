function solution(arr) {
    var answer = 0;
    
    let a = arr[0]

    for (let i = 1; i < arr.length; i++) {
        b = LCM(a, arr[i])
        a = b
    }
    
    return a;
}

function GCD(x, y){
    while (y) {
        let z = x
        x = y
        y = z % y
    }
    return x
}

function LCM(x, y){
    return x * y / GCD(x, y)
}