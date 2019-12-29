var input = require('fs').readFileSync('/dev/stdin','utf8');
var lines = input.split('\n');

let letra = /[a-zA-Z]/;

while (true) {
  let entrada = lines.shift();
  let upper = true;

  if( !entrada )
    break;

  entrada = entrada.split("");

  for (let i = 0; i < entrada.length; i++) {
    if (letra.test(entrada[ i ])) {
      if (upper) {
        entrada[i] = entrada[i].toString().toUpperCase();
      } else {
        entrada[i] = entrada[i].toString().toLowerCase();
      }
      upper = !upper;
    }
  }

  console.log(entrada.join(""));
}