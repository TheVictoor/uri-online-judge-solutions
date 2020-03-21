var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let entrada = lines.shift();
let [pote1, pote2, pote3, pote4] = entrada.trim().split(" ");

if( pote1 == "1" ){
  console.log(1);
} else if (pote2 == "1") {
  console.log(2);
} else if (pote3 == "1") {
  console.log(3);
} else if (pote4 == "1") {
  console.log(4);
}