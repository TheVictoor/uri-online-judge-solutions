let input = require('fs').readFileSync('/dev/stdin', 'utf8');
let lines = input.split('\n');

let groups = parseInt( lines.shift() );

function toBinary( value ) {
    if( value <= 1 ){
        return value.toString();
    }else {
        return toBinary( Math.trunc(value / 2 )) + ( value % 2 ).toString();
    }
}

for( let i = 0; i < groups; i++ ){
    
    let binaryStream = toBinary( parseInt(lines[i]) );
    let sequence = 0;
    let hit = 0;

    for( let l = 0; l < binaryStream.length; l++ ){

        if( binaryStream[l] == "1" ){
            hit++;
            if( hit > sequence )
                sequence = hit;
        }else {
            hit = 0;
        }

    }    

    console.log( sequence );

}