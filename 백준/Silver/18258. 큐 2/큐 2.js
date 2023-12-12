let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

class Queue {
    constructor() {
        this.q = []
        this.start = 0
        this.end = 0
    }
    push(value) {
        this.q[this.end] = value
        this.end++
    }
    
    pop() {
        if (this.start < this.end) {
            const x = this.q[this.start]
            this.start++ 
            return x
        } else {
            return -1
        }
    }
    size() {
        return this.end - this.start
    }
    empty() {
        if (this.start < this.end) {
            return 0
        } else {
            return 1
        }
    }
    front() {
        if (this.start < this.end) {
            const x = this.q[this.start]
            return x
        } else {
            return -1
        }
    }
    back() {
        if (this.start < this.end) {
            const x = this.q[this.end-1]
            return x
        } else {
            return -1
        }
    }

}

let q = new Queue()
let result = ""

let start = 0
let end = 0

for(let i = 1; i < parseInt(input[0])+1; i++) {
    let line = input[i].split(" ")
    let word = line[0].trim()

    if (word === 'push') {
        q.push(parseInt(line[1]))
    } else if (word === 'pop') {
        result += q.pop() + "\n"
    } else if (word === 'size') {
        result += q.size()  + "\n"
    } else if (word === 'empty') {
        result += q.empty() + "\n"
    } else if (word === 'front') {
        result += q.front() + "\n"
    } else if (word === 'back') {
        result += q.back() + "\n"
    }

}
console.log(result)