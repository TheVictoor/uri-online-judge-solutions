var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

var dataEntrega;
var dataLimteVerificacao;
var datas;

datas = lines.shift().split( " " );

dataEntrega = parseInt( datas[ 0 ] );
dataLimteVerificacao = parseInt( datas[ 1 ] );

if ( dataEntrega > dataLimteVerificacao ) {
    console.log( "Eu odeio a professora!" );
} else {

    if ( dataLimteVerificacao - dataEntrega >=   3 ) {
        console.log( "Muito bem! Apresenta antes do Natal!" );
    } else {

        var msg = "Parece o trabalho do meu filho!\n";

        if ( dataLimteVerificacao + 2 <= 24 ){
            msg += "TCC Apresentado!";
        }else {
            msg += "Fail! Entao eh nataaaaal!";
        }

        console.log( msg );

    }

}
