var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let casos = parseInt( lines.shift() );
let reg = /<(.*?)>/;

for ( let i = 0; i < casos; i++ ) {
  let diamantes = 0;
  let entrada = lines.shift();
  while ( reg.test( entrada ) ) {
    ++diamantes
    entrada = entrada.replace( reg, "$1" ); 
  }
  console.log( diamantes );
}