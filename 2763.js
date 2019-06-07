var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let cpf = lines.shift();
cpf = cpf.replace( '-' , '.' );
cpf = cpf.split( '.' );

cpf.forEach(item => {
    console.log( item );
});
