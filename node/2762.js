var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );
var numero = lines.shift();

numero = numero.replace( /([0-9]+)\.([0-9]+)/ , "$2.$1" );
console.log( numero.replace( /^0/gi , "" ) );