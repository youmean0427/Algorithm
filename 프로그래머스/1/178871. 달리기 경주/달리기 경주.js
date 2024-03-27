function solution(players, callings) {
    var answer = [];
    let price = {}
    let name = {}
    
    for (let i = 0; i <players.length; i++) {
        name[players[i]] = i+1
        price[i+1] = players[i]
    }
    
    for (let i = 0; i < callings.length; i++) {
        let x = name[callings[i]] // price
        let y = price[x-1] // name
        price[x] = y
        price[x-1] = callings[i]
        name[y] = x
        name[callings[i]] = x-1
    }
    
    const res = Object.entries(price)
    res.forEach(x => answer.push(x[1]))
    return answer;
}