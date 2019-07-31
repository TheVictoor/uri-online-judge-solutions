let input = require('fs').readFileSync('/dev/stdin', 'utf8');
let lines = input.split('\n');

while( lines.length >= 4 ){

    let nPalavras = 0;
    let palavras = [];
    let nConsultas = 0;
    let consultas = [];

    nPalavras = parseInt( lines.shift() );

    for( let i = 0; i < nPalavras; i++ ){
        palavras.push( lines.shift() );
    }

    nConsultas = parseInt( lines.shift() );

    for( let i = 0; i < nConsultas; i++ ){
        consultas.push( lines.shift() );
    }
    
    for( let consulta of consultas ){
        let size = 0;
        let ocorrencias = 0;
        let reg = new RegExp( `${consulta}` );

        for( let palavra of palavras ){
            let ret = reg.test( palavra );

            if( ret ){
                size  = size > palavra.length ? size : palavra.length;
                ocorrencias++;
            }
        }

        if( size == 0 && ocorrencias == 0 ){
            console.log( -1 );
        }else {
            console.log(`${ocorrencias} ${size}`);
        }

    }

}