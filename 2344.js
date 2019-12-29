var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let nota = parseInt(lines.shift());

if( nota == 0 )
  console.log("E");
else if( nota < 36 )
  console.log("D");
else if( nota < 61 )
  console.log("C");
else if( nota < 86 )
  console.log("B");
else 
  console.log("A");