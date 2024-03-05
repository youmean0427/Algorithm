let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input.toString().trim().split("\n");

for (let i = 0; i < input.length; i++) {
  if (input[i] !== "END") {
    let s = input[i].trim().split(" ");
    s.reverse();
    ans = [];
    for (let j = 0; j < s.length; j++) {
      let x = s[j].split("");
      x.reverse();
      ans.push(x.join(""));
    }
    console.log(ans.join(" "));
  } else {
    break;
  }
}
