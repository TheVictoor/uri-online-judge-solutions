var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

for ( let index = 97; index < 123; index++ ) {
  console.log( `${ index } e ${ String.fromCharCode( index ) }` );
}