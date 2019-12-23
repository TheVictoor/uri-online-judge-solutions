var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let [distancia, diametro1, diametro2 ] = lines[0].split(" ");
let ICM = parseInt( distancia ) / ( parseInt( diametro1 ) + parseInt( diametro2 ) );

console.log( ICM.toFixed(2) );