var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
let status = false;

let keyMaps = {
    "a" : "1",
    "b" : "2",
    "c" : "3",
    "d" : "4",
    "e" : "5",
    "f" : "6",
    "g" : "7",
    "h" : "8"
};

lines = lines[0].toString();

lines = lines
    .replace(  /[A-H]/gi, ( match ) => keyMaps[ match ] );

let [ origem , destino ] = lines.split(" ");

origem = origem.split("");
destino = destino.split("");

origem = origem.map( (i) => parseInt(i) );
destino = destino.map( (i) => parseInt(i) );

if ( destino[0] - 2 == origem[0] && destino[1] - 1 == origem[1] ){ // ok
    status = true;
} else if ( destino[0] - 1 == origem[0] && destino[1] - 2 == origem[1] ){ // ok
    status = true;
} else if ( destino[0] - 2 == origem[0] && destino[1] + 1 == origem[1] ){ // ok
    status = true;
} else if ( destino[0] - 1 == origem[0] && destino[1] + 2 == origem[1] ){ // ok
    status = true;
} else if ( destino[0] + 1 == origem[0] && destino[1] - 2 == origem[1] ){ // ok
    status = true;
} else if ( destino[0] + 2 == origem[0] && destino[1] - 1 == origem[1] ){ // ok
    status = true;
} else if ( destino[0] + 1 == origem[0] && destino[1] + 2 == origem[1] ){ // ok
    status = true;
} else if ( destino[0] + 2 == origem[0] && destino[1] + 1 == origem[1] ){ // ok
    status = true;
} 

if(status){
    console.log("VALIDO");
}else {
    console.log( "INVALIDO" );
}