var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let casos = parseInt(lines.shift());
let instancia = 1;

while (casos-- > 0) {
  let matrix = [];
  let status = true;

  for (let i = 0; i < 9; i++) matrix.push(normalize(lines.shift().split(' ')));

  for (let i = 0; i < 9; i++) {
    let row = matrix[i];
    let retorno = validateEntries([...row]);
    if (!retorno) {
      status = false;
      break;
    }
  }

  if (status) {
    for (let i = 0; i < 9; i++) {
      let col = matrix.map(row => row[i]);
      let retorno = validateEntries([...col]);
      if (!retorno) {
        status = false;
        break;
      }
    }
  }

  if (status) {
    for (let i = 0; i < 9; i++) {
      let entries = selectRange(matrix, i);
      let retorno = validateEntries([...entries]);
      if (!retorno) {
        status = false;
        break;
      }
    }
  }

  console.log("Instancia " + instancia++);
  if(status){
    console.log("SIM");
  } else {
    console.log("NAO");
  }
  console.log("");

}

function validateEntries(entries) {
  if (entries.length != 9)
    return false;

  let state = true;

  entries.sort((a, b) => a - b);

  entries.forEach((item, index) => {
    if (item != index + 1) {
      state = false;
      return false;
    }
  });

  return state;
}

function normalize(items) {
  return items.map(i => parseInt(i));
}

function selectRange(matrix, range) {
  if(range == 0){
    return [matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2]];
  } else if ( range == 1 ) {
    return [matrix[0][3], matrix[0][4], matrix[0][5], matrix[1][3], matrix[1][4], matrix[1][5], matrix[2][3], matrix[2][4], matrix[2][5]];
  } else if ( range == 2 ) {
    return [matrix[0][6], matrix[0][7], matrix[0][8], matrix[1][6], matrix[1][7], matrix[1][8], matrix[2][6], matrix[2][7], matrix[2][8]];
  } else if ( range == 3 ) {
    return [matrix[3][0], matrix[3][1], matrix[3][2], matrix[4][0], matrix[4][1], matrix[4][2], matrix[5][0], matrix[5][1], matrix[5][2]];
  } else if ( range == 4 ) {
    return [matrix[3][3], matrix[3][4], matrix[3][5], matrix[4][3], matrix[4][4], matrix[4][5], matrix[5][3], matrix[5][4], matrix[5][5]];
  } else if ( range == 5 ) {
    return [matrix[3][6], matrix[3][7], matrix[3][8], matrix[4][6], matrix[4][7], matrix[4][8], matrix[5][6], matrix[5][7], matrix[5][8]];
  } else if ( range == 6 ) {
    return [matrix[6][0], matrix[6][1], matrix[6][2], matrix[7][0], matrix[7][1], matrix[7][2], matrix[8][0], matrix[8][1], matrix[8][2]];
  } else if ( range == 7 ) {
    return [matrix[6][3], matrix[6][4], matrix[6][5], matrix[7][3], matrix[7][4], matrix[7][5], matrix[8][3], matrix[8][4], matrix[8][5]];
  } else if ( range == 8 ) {
    return [matrix[6][6], matrix[6][7], matrix[6][8], matrix[7][6], matrix[7][7], matrix[7][8], matrix[8][6], matrix[8][7], matrix[8][8]];
  } 
}
