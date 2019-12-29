var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let casos = parseInt( lines.shift() );

for ( let i = 0; i < casos; i++ ) {
  let entrada = lines.shift();
  let [str, valor] = entrada.split(" ");
  let reg = new RegExp( `${valor}$` );

  if( reg.test( str ) ) 
    console.log( "encaixa" );
  else 
    console.log( "nao encaixa" );
}