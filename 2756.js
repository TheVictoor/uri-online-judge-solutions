var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

console.log(`       A
      B B
     C   C
    D     D
   E       E
    D     D
     C   C
      B B
       A`)