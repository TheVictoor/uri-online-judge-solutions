var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let quantidadeTeste = lines.shift();

for ( let i = 0; i < quantidadeTeste; i++ ) {
  let entrada = lines.shift();
  let [ compradas, paraTroca ] = entrada.trim().split( " " );

  compradas = parseInt( compradas );
  paraTroca = parseInt( paraTroca );

  if ( compradas < paraTroca ) {
    console.log( compradas )
  } else {
    let bebidas = compradas;
    while ( true ) {
      let resultado = bebidas % paraTroca;
      if ( resultado == 0 ) {
        console.log( ( compradas - bebidas ) + ( bebidas / paraTroca ) );
        break;
      }
      --bebidas;
    }
  }
}