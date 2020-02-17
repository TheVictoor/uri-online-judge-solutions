var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let colocacao = parseInt(lines.shift());
let resultado = 10

if (colocacao <= 1) resultado = 1;
else if (colocacao <= 3) resultado = 3;
else if (colocacao <= 5) resultado = 5;
else if (colocacao <= 10) resultado = 10;
else if (colocacao <= 25) resultado = 25;
else if (colocacao <= 50) resultado = 50;
else if (colocacao <= 100) resultado = 100;

console.log('Top ' + resultado);