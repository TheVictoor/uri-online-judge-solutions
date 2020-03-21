var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let regras = "";
let palavras = "";

regras = lines.shift();
palavras = lines.shift();

do {

    let limiteCaracteresLinha = 0;
    let limiteLinhasPagina = 0;
    let paginasUsadas = 1;
    let linhaAtual = 1;
    let caracteresUtual = 0;

    limiteLinhasPagina = regras.split( " " )[1];
    limiteCaracteresLinha = regras.split( " " )[2];

    // TRANSFORMAR A STRING EM UM ARRAY
    palavras = palavras.split( " " ) || [];

    palavras.forEach(palavra => {
        
        if( caracteresUtual + palavra.length <= limiteCaracteresLinha ){

            caracteresUtual += palavra.length;

            // COLOCAR ESPACO APOS AS PALAVRAS
            if( caracteresUtual + 1 <= limiteCaracteresLinha ){
                caracteresUtual++;                    
            }

        }else{

            if( linhaAtual == limiteLinhasPagina ){
                
                caracteresUtual = palavra.length;

                if( caracteresUtual + 1 <= limiteCaracteresLinha ){
                    caracteresUtual++;                    
                }

                linhaAtual = 1;
                paginasUsadas++;

            }else{

                caracteresUtual = palavra.length;

                if( caracteresUtual + 1 <= limiteCaracteresLinha ){
                    caracteresUtual++;                    
                }

                linhaAtual++;

            }

        }

    });

    console.log( paginasUsadas );

    regras = lines.shift();
    palavras = lines.shift();   

} while ( regras && palavras )