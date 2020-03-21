var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let data = lines.shift();
let [dd, mm, aa] = data.split(/\D/g);

console.log(`${mm}/${dd}/${aa}`);
console.log(`${aa}/${mm}/${dd}`);
console.log(`${dd}-${mm}-${aa}`);