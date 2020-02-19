var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let changeByZero = /o/gi;
let changeByOne = /l/g;
let removeEntities = /[,\s]/g;
let invalidEntities = /[^0-9]/;
let removeLeftZero = /^0{1,}/gi;

const LIMIT = 2147483647;

function checkRange(value, start = 0, end = LIMIT){
  if(!value)
    return false;

  if(value.length > 10)
    return false;

  let convertedValue = parseInt(value);
  return convertedValue >= start && convertedValue <= end;
}

lines.pop();

while(lines.length != 0){
  let value = lines.shift();

  value = value.replace(changeByZero, '0');
  value = value.replace(changeByOne, '1');
  value = value.replace(removeEntities, '');
  value = value.replace(removeLeftZero, '0');

  if(invalidEntities.test(value) || value.length == 0){
    console.log('error');
    continue;
  }

  const result = checkRange(value);

  if (!result) {
    console.log('error');
    continue;
  }

  console.log(parseInt(value));
}
