var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let line1 = lines.shift().split(" ");
let line2 = lines.shift().split(" ");

let soma = 0;

for( let i = 0; i < line1.length; i++ ){
  if( parseInt(line1[i]) < parseInt(line2[i]) )
    soma += parseInt(line2[i]) - parseInt(line1[i]);
}

console.log(soma);