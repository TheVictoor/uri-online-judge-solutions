var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let entrada = lines.shift();
let [porta1, porta2] = entrada.trim().split(" ");

if( porta1 == "0" )
  console.log("C");
else {
  if( porta2 == "0" )
    console.log("B");
  else 
    console.log("A");
}