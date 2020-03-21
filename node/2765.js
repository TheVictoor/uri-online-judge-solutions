var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );
var frase = lines.shift();
var partes = [];
var partesFinal = [];
var verify = 0;

partes = frase.split( ',' );

partes.forEach( item => {

    if ( verify < 2 ) {
        partesFinal.push( item );
        verify++;
    } else {
        partesFinal[ 1 ] += ',' + item;
    }

} );

partesFinal.forEach( i => {
    console.log( i );
} );