var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

while ( lines.length >= 3 ) {

    // VARIAVEIS COM VALORES
    var nNumeros = parseInt( lines.shift() );
    var arrayNumeros = lines.shift().split( ' ' );
    var nNumeroSorte = lines.shift();
    

    if( arrayNumeros.indexOf( nNumeroSorte ) == 0 ){
        console.log( "Y" );
    }else{

        var resposta = "N";
        var nIncremento = 2;

        while ( 1 ) {

            var indexRemove = 0; // ITEM 2
            indexRemove = nIncremento;
    
            arrayNumeros = arrayNumeros.filter( ( item, indice ) => {
                if ( ( indice + 1 ) == indexRemove ) {
                    indexRemove += nIncremento;
                    return false;
                } else {
                    return true;
                }
            } );
    
            nIncremento++;
    
            // console.log( arrayNumeros.join( ', ' ) );
            // console.log(`index to remove = ${ nIncremento } ` );
            // console.log( arrayNumeros.indexOf( nNumeroSorte ) );
    
            if ( arrayNumeros.indexOf( nNumeroSorte ) == -1 ) {
                break;
            }
    
            if ( arrayNumeros.indexOf( nNumeroSorte ) + 1 < nIncremento ) {
                resposta = "Y";
                break;
            }
    
        }
    
        console.log( resposta );

    }

}