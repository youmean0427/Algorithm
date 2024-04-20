let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input.toString().trim().split("\n");

const n = parseInt(input[0]);
const [sn, en] = input[1].split(" ").map((x) => parseInt(x));
const m = parseInt(input[2]);

let arr = Array.from({ length: n + 1 }, () => new Array());

for (let i = 3; i < input.length; i++) {
  const [a, b] = input[i].split(" ").map((x) => parseInt(x));
  arr[a].push(b);
  arr[b].push(a);
}

function bfs(sn) {
  let q = [[sn, 0]];
  let visited = new Array(n + 1).fill(0);
  while (q.length) {
    const [x, y] = q.shift();

    if (x === en) {
      return y;
    }

    arr[x].forEach((x) => {
      if (visited[x] === 0) {
        visited[x] = 1;
        q.push([x, y + 1]);
      }
    });
  }
  return -1;
}

const ans = bfs(sn);
console.log(ans);
