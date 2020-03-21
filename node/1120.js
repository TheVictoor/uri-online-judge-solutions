var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

{
    let valores = [...lines];

    while( 1 ){

        let current = valores.shift();
        let digitoProblematico = current.split( " " )[0];
        let valorContrato = current.split( " " )[1];
        let valorImpresso = "";
        let regexp = /^0/g;

        if( digitoProblematico == "0" && valorContrato == "0" ){
            break;
        }

        // REMOVE TODOS OS VALORES CORREPONDETES AO DIGITO DEFEITUOSO
        valorContrato = valorContrato.replace( new RegExp( digitoProblematico, "g" ) , "" );  

        // REMOVE TODOS OS NUMEROS 0 A ESQUERDA
        while( regexp.test( valorContrato ) ){
            valorContrato = valorContrato.replace( regexp , "" );
        }

        valorImpresso = valorContrato == "" ? "0" : valorContrato; 

        console.log( valorImpresso );

    }    
}