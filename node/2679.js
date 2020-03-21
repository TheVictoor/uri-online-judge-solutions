var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let valor = parseInt( lines.shift() );

if ( valor & 1 )
  console.log( valor + 1 );
else
  console.log( valor + 2 );
  