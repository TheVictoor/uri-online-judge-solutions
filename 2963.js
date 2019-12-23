var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let participantes = lines.shift();
let carlos = parseInt(lines.shift());
let votos = [...lines];
let resposta = "S";

participantes = parseInt( participantes );
--participantes;

for( let i = 0; i < participantes; i++ ){
  if( parseInt(votos[i]) > carlos){
    resposta = "N";
    break;
  }
}

console.log( resposta );