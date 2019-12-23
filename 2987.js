var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );
let posicao = lines.shift().charCodeAt(0);
console.log( posicao - 64 );