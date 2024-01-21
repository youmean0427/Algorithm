function solution(priorities, location) {
    var answer = 0;
    
    let arr = []
    
    priorities.forEach((x, idx) => {
        arr.push([x, idx]) 
    })
    
    let result = []
    while (arr.length) {
        let x = arr.shift()
        let check = 0
        for (let i of arr) {
            if (x[0] < i[0]) {
                check = 1
            }
        }
        
        if (check === 1) {
            arr.push(x)
        } else {
            result.push(x[1])
        }    
    }

    result.forEach((i, idx) => {
        if (i === location) {
            answer = idx+1
            return
        }
    })
    
    return answer;
}