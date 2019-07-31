let input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
let lines = input.split( '\n' );

while ( lines.length >= 3 ) {
    let nPacotes = parseInt( lines.shift() );
    let pacotes = lines.shift().split( " " );
    let tempoPacotes = lines.shift().split( " " );
    let tempoTotal = 0;

    pacotes = pacotes.map( i => parseInt( i ) );
    tempoPacotes = tempoPacotes.map( i => parseInt( i ) );

    for ( let i = 0; i < nPacotes - 1; i++ ) {
        for ( let j = 1; j < nPacotes - i; j++ ) {
            if ( pacotes[ j - 1 ] > pacotes[ j ] ) {
                let aux;
                tempoTotal += ( tempoPacotes[ j - 1 ] + tempoPacotes[ j ] );

                aux = tempoPacotes[ j - 1 ];
                tempoPacotes[ j - 1 ] = tempoPacotes[ j ];
                tempoPacotes[ j ] = aux;

                aux = pacotes[ j - 1 ];
                pacotes[ j - 1 ] = pacotes[ j ];
                pacotes[ j ] = aux;

            }
        }
    }
    console.log( tempoTotal );
}
