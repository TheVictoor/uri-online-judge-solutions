var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let tentativas;
let menorTempo = 0.0;

while ( tentativas = lines.shift() ) {

    for ( var i = 0; i < tentativas; i++ ) {
        let tempoFeito = parseFloat( lines.shift() );
        if( menorTempo == 0 || tempoFeito < menorTempo ){
            menorTempo = tempoFeito;
        }
    }

    console.log( menorTempo );
    menorTempo = 0.0;

}