var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let regVogal = /^[aeiou]/gi;
let regBlankSpace = /\s/g;
let regIsLetter = /[a-z]/gi;
let [ cifra , nMessages, ...messages ] = lines;

cifra = cifra.replace( regBlankSpace , "" );
nMessages = parseInt(nMessages);

for( let i = 0; i < nMessages; i++ ){
    messages[i] = messages[i].replace( /\s{1,}/g , " " );
    messages[i] = messages[i].replace( /\s$|^\s/g , "" );

    let [ ...words ] = messages[i].split( " " );
    let startConsoante;
    let cryptWords = [];
    let indexCrypt = 0;
    
    for (let word of words) {

        let crypted = [];
        startConsoante = false;
        startConsoante = !/^[aeiou]/gi.test( word.toString() );

        for (const letter of word) {
            if( startConsoante ){
                if( indexCrypt >= cifra.length ){
                    indexCrypt = 0;
                }
                crypted.push( getLetter( cifra[ indexCrypt ] , letter ) );
                ++indexCrypt;
            }else {
                crypted.push( letter.toLowerCase() );
            }
        }  

        cryptWords.push( crypted.join("") );
    }

    console.log( cryptWords.join(" ") );
}

function getLetter( cifra, letter ){

    let asciiCodeCifra = cifra.toUpperCase().charCodeAt(0);
    let asciiCodeLetter = letter.toUpperCase().charCodeAt(0);
    let move = (asciiCodeCifra - 65);

    if( (asciiCodeLetter + move) > 90 ){
        asciiCodeLetter -= 26;
    }

    asciiCodeLetter += move;

    return String.fromCharCode( asciiCodeLetter ).toLowerCase();

}
