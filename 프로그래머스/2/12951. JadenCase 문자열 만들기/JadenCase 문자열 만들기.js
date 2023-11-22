function solution(s) {
    var answer = []
    let arr = s.split("")
    let check = 1

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] != ' ' && check == 1) {
            arr[i] = arr[i].toUpperCase()
            check = 0
        } else if(arr[i] == ' ') {
            check = 1
        } else {
            arr[i] = arr[i].toLowerCase()
        }
    }
    answer = arr.join("")

    return answer
}