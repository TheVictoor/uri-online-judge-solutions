var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let arrayValor = lines.shift().split( " " );

arrayValor.forEach( i => i = parseInt( i ) );
arrayValor.sort( (a, b) => b - a );

console.log( arrayValor[0] );