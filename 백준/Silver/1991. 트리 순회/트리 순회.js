let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input.toString().trim().split("\n");

const N = parseInt(input[0]);
arr = Array.from({ length: N + 1 }, () => []);
for (let i = 1; i <= N; i++) {
  const [P, L, R] = input[i].split(" ").map((x) => x.charCodeAt() - 64);

  if (L > 0) {
    arr[P].push(L);
  } else {
    arr[P].push(".");
  }

  if (R > 0) {
    arr[P].push(R);
  } else {
    arr[P].push(".");
  }
}

preVal = "";
function Preorder(x) {
  if (x !== ".") {
    let point = x + 64;
    preVal += String.fromCodePoint(point);
    Preorder(arr[x][0]);
    Preorder(arr[x][1]);
  }
}

Preorder(1);
console.log(preVal);

inVal = "";
function Inorder(x) {
  if (x !== ".") {
    Inorder(arr[x][0]);
    let point = x + 64;
    inVal += String.fromCodePoint(point);
    Inorder(arr[x][1]);
  }
}

Inorder(1);
console.log(inVal);

postVal = "";
function Postorder(x) {
  if (x !== ".") {
    Postorder(arr[x][0]);
    Postorder(arr[x][1]);
    let point = x + 64;
    postVal += String.fromCodePoint(point);
  }
}

Postorder(1);
console.log(postVal);
