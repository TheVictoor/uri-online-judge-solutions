var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let casos = parseInt( lines.shift() );

for ( let i = 0; i < casos; i++ ) {
  let entrada = lines.shift();
  let quantidade = 0;

  entrada = parseFloat( entrada );

  while( entrada > 1.0 ){
    quantidade++;
    entrada = entrada / 2;
  }

  console.log( `${quantidade} dias` );
}
