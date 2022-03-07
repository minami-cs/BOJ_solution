let fs = require("fs");
let num = Number(fs.readFileSync("/dev/stdin").toString().trim());
console.log(num - 543);

// function solution(n) {
//   return n - 543;
// }

// console.log(solution(2541));
