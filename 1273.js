var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
var casosTeste = 0;
var first = true;

{

    while( (casosTeste = lines.shift()) != 0 ){

        let maiorComprimento = 0;
        let valores = [];

        if( !first ) console.log( "" );

        // COLOCA NO ARRAY OS VALORES QUE SERAO USADOS NESSE CASO DE TESTE
        for( var i = 0; i < casosTeste; i++ ){
            valores.push( lines.shift() );
        }

        valores.forEach(item => {
            maiorComprimento = maiorComprimento < item.length ? item.length : maiorComprimento;
        });        

        valores.forEach(item => {
            
            let spaceNumber = maiorComprimento - item.length;
            let spaceChars = "";

            while( spaceNumber > 0){
                spaceChars += " ";
                spaceNumber--;
            }

            console.log( `${spaceChars}${item}` );

        });

        first = false;

    }

}