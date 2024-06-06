var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");
let [a, b, c] = lines.shift().split(" ").map(Number);
const p = (a + b + c) / 2;
const area = Math.sqrt(p * (p - a) * (p - b) * (p - c));
console.log(area.toFixed(3) + " m2");
