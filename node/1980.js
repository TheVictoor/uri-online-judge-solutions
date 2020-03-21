var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let respostas = {
	'0': 1,
	'1': 1,
	'2' : 2,
	'3' : 6,
	'4' : 24,
	'5' : 120,
	'6' : 720,
	'7' : 5040,
	'8' : 40320,
	'9' : 362880,
	'10' : 3628800,
	'11' : 39916800,
	'12' : 479001600,
	'13' : 6227020800,
	'14' : 87178291200,
	'15' : 1307674368000,
};

while(true){
	let word = lines.shift();
	if(word === '0') break;
	
	word = word.replace(/\s/gi, "");
	console.log(respostas[word.length]);
}