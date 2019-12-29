var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let casos = parseInt( lines.shift() );

for ( let i = 0; i < casos; i++ ) {
  let entrada = lines.shift();
  let message = "";
  entrada = parseInt( entrada );

  let resultado = isPrime( entrada );

  if ( resultado )
    message = "Prime";
  else
    message = "Not Prime";

  console.log( message );
}

function isPrime( num ) {
  var isPrime = true;
  if ( num >= 2 ) {
    if ( num == 2 || num == 3 ) {
      isPrime = true;
    } else if ( num % 2 == 0 ) {
      isPrime = false;
    } else {
      for ( i = 3; i <= Math.floor( Math.sqrt( num ) ); i += 2 ) {
        if ( num % i == 0 ) {
          isPrime = false;
          break;
        }
      }
    }
  } else {
    isPrime = false;
  }
  return isPrime;
}