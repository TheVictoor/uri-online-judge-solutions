var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let times = parseInt( lines.shift() );

for ( let i = 0; i < times; i++ ) {
  let [ x, y ] = lines[ i ].split( " " );
  x = parseInt( x );
  y = parseInt( y );

  let z = x**y;

  console.log(z.toLocaleString().replace( /\W/g, "" ).length);
}