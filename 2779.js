let input = require('fs').readFileSync('/dev/stdin', 'utf8');
let lines = input.split('\n');
let [ nFiguras , nFigurasCompradas ] = lines;
let setFiguras = new Set();

lines.shift();
lines.shift();

for( let i = 0; i < nFigurasCompradas; i++ ){
    setFiguras.add( parseInt( lines[i] ) );
}

console.log( nFiguras - setFiguras.size );