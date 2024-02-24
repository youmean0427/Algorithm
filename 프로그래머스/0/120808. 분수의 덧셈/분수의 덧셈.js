function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    
    let denom = denom1 * denom2
    let numer3 = numer1 * denom2
    let numer4 = numer2 * denom1
    let numer = numer3 + numer4
    
    const GCD = (x, y) => {
        while (y) {
            t = y
            y = x % y
            x = t
        }    
        return x
    }
    
    let g = GCD(denom, numer)
    answer = [numer / g, denom / g ]
    
    return answer;
}