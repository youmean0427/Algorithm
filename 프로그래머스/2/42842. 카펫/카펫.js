function solution(brown, yellow) {

    start = Math.trunc(brown/4)
    end = Math.ceil(brown/2)
    
    total = brown + yellow
    arr = []
    for (let i = start; i < end; i++) {
        if (total % i == 0 && i > 2) {
           arr.push([i, total / i]) 
        }    
    }
    var answer = []
    for (x of arr) {
        x.sort((a, b) => b - a)
        if (x[0] * 2 + (x[1] - 2) * 2 === brown) {
            answer = x    
        }
    }
    
    return answer
}

// 14	4	None	[6, 3]
// 18	6	None	[8, 3]
// 20	12	None	[8, 4]
// 22	8	None	[10, 3]
// 24	9	None	[11, 3]
// 24	16	None	[10, 4]
// 26	10	None	[12, 3]