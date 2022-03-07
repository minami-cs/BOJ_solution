let fs = require("fs");
let str = fs.readFileSync("/dev/stdin").toString().trim();
console.log(`${str}??!`);

// function solution(str) {
//   return str + "??!";
// }
// console.log(solution("skdfls"));
