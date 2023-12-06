let fs = require('fs').readFileSync('/dev/stdin').toString().trim().split('');
const number = {
    ABC : 3,
    DEF : 4,
    GHI : 5,
    JKL : 6,
    MNO : 7,
    PQRS : 8,
    TUV : 9,
    WXYZ : 10
}

const dial = fs;
let sum = 0;

for(let i=0; i<dial.length; i++){
    for(let x in number){
        if(x.includes(dial[i])){
            sum += number[x];
        }
    }
}
console.log(sum);