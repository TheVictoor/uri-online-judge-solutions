const input = require("fs").readFileSync("/dev/stdin", "utf8");
const lines = input.split("\n");

lines.shift();
lines.shift();
let trees = {};
let total = 0;

let l = lines.length - 1;
let c = 0;

while (c < l) {
  const line = lines[c].trim();
  c += 1;

  if (line.length == 0) {
    const keys = Object.keys(trees).sort();
    keys.forEach((k) => {
      const percentage = ((trees[k] * 100) / total).toFixed(4);
      console.log(`${k} ${percentage}`);
    });
    console.log("");

    trees = {};
    total = 0;

    continue;
  }

  if (trees[line]) {
    trees[line] += 1;
  } else {
    trees[line] = 1;
  }
  total += 1;
}

const keys = Object.keys(trees).sort();
keys.forEach((k) => {
  const percentage = ((trees[k] * 100) / total).toFixed(4);
  console.log(`${k} ${percentage}`);
});
