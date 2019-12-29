var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

while (true) {

  let entrada = lines.shift();

  if (!entrada)
    break;

  let [ valor1, valor2 ] = entrada.split(" ");

  valor1 = parseInt(valor1)
  valor2 = parseInt(valor2)

  if (valor1 > valor2)
    console.log(valor1 - valor2);
  else
    console.log(valor2 - valor1);

}