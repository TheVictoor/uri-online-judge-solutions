var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

const qwertyLeftMap = {
  1: "`",
  2: "1",
  3: "2",
  4: "3",
  5: "4",
  6: "5",
  7: "6",
  8: "7",
  9: "8",
  0: "9",
  "-": "0",
  "=": "-",
  Q: "`",
  W: "Q",
  E: "W",
  R: "E",
  T: "R",
  Y: "T",
  U: "Y",
  I: "U",
  O: "I",
  P: "O",
  "[": "P",
  "]": "[",
  "\\": "]",
  A: "`",
  S: "A",
  D: "S",
  F: "D",
  G: "F",
  H: "G",
  J: "H",
  K: "J",
  L: "K",
  ";": "L",
  "'": ";",
  Z: "`",
  X: "Z",
  C: "X",
  V: "C",
  B: "V",
  N: "B",
  M: "N",
  ",": "M",
  ".": ",",
  "/": ".",
  "`": "`",
  " ": " ",
  "!": "`",
  "@": "!",
  "#": "@",
  $: "#",
  "%": "$",
  "^": "%",
  "&": "^",
  "*": "&",
  "(": "*",
  ")": "(",
  _: ")",
  "+": "_",
  "{": "P",
  "}": "{",
  "|": "}",
  ":": "L",
  '"': ":",
  "<": "M",
  ">": "<",
  "?": ">",
};

function translateInput(input) {
  return input
    .split("")
    .map((char) => qwertyLeftMap[char] || char)
    .join("");
}

while (lines.length > 1) {
  const input = lines.shift();
  const output = translateInput(input);
  console.log(output);
}
