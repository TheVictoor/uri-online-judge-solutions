var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

{
    let LEDsByNumber = {
        "0" : 6, 
        "1" : 2,
        "2" : 5,
        "3" : 5, 
        "4" : 4, 
        "5" : 5, 
        "6" : 6, 
        "7" : 3, 
        "8" : 7, 
        "9" : 6
    };

    let numeroTestes =  parseInt(lines.shift());

    while( numeroTestes > 0 ){

        let LEDsUsados = 0;
        let casoTeste = lines.shift();
        casoTeste = casoTeste.split("");
        casoTeste = casoTeste || []; 

        casoTeste.forEach(item => {
            LEDsUsados += LEDsByNumber[ item ];                
        });

        console.log( `${LEDsUsados} leds` );

        numeroTestes--;

    }

}