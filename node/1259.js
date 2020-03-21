var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let casos = parseInt(lines.shift());
let valores = [];
let par = [];
let impar = [];

for (let i = 0; i < casos; i++) {
  let entrada = lines.shift();
  entrada = parseInt(entrada);

  if (entrada & 1)
    impar.push(entrada);
  else
    par.push(entrada);
}

impar.sort((a, b) => b - a);
par.sort((a, b) => a - b);
valores = [ ...par, ...impar ];

valores.forEach(valor => console.log(valor));