let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input.toString().trim();

const N = parseInt(input[0]);
let arr = new Array(N + 1).fill(0).map((x, i) => (x = i));

if (arr.length <= 2) {
  box = arr;
}
while (arr.length > 2) {
  box = [];
  arr.forEach((x, i) => {
    if (i % 2 == 0) {
      box.push(x);
    }
  });
  arr = box;
}

console.log(box[1]);
