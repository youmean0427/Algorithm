function solution(brown, yellow) {

    const start = Math.trunc(brown/4)
    const end = Math.ceil(brown/2)
    
    const total = brown + yellow
    
    let test = []
    for (let i = start; i < end; i++) {
        if (total % i == 0 && i > 2) {
           test.push([i, total / i]) 
        }    
    }
    
    var answer = []
    for (let x of test) {
        x.sort((a, b) => b - a)
        if (x[0] * 2 + (x[1] - 2) * 2 === brown) {
            answer = x    
        }
    }
    
    return answer
}

// Test
// 14	4	[6, 3]
// 18	6	[8, 3]
// 20	12	[8, 4]
// 22	8	[10, 3]
// 24	9	[11, 3]
// 24	16	[10, 4]
// 26	10	[12, 3]