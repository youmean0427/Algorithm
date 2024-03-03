let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input.toString().trim().split("\n");

const T = parseInt(input[0]);
idx = 1;
while (idx < input.length) {
  let [J, N] = input[idx].split(" ").map((x) => parseInt(x));
  arr = new Array();
  let i = idx + 1;
  while (i <= N + idx) {
    const [R, C] = input[i].split(" ").map((x) => parseInt(x));
    arr.push(R * C);
    i += 1;
  }
  arr.sort((a, b) => a - b);
  ans = 0;
  while (J > 0) {
    x = arr.pop();
    J -= x;
    ans += 1;
  }
  console.log(ans);
  idx += N + 1;
}
