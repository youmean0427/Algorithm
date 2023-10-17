function solution(dot) {
    const position = [[1, 4], [2, 3]]
    let positionIdx = 0
    var answer = 0;

    const x = dot[0]
    const y = dot[1]

    if (x > 0) {
        positionIdx = 0
        
        if (y > 0) {
            answer = position[positionIdx][0]
        }
        else {
            answer = position[positionIdx][1]
        }
        
    }
    else {
        positionIdx = 1
                
        if (y > 0) {
            answer = position[positionIdx][0]
        }
        else {
            answer = position[positionIdx][1]
        }
    }
    
    return answer;
}