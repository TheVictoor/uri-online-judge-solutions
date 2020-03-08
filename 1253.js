var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let casosTeste = parseInt(lines.shift());

for (let i = 0; i < casosTeste; i++) {
	let cifra = lines.shift();
	let chave = parseInt(lines.shift());

	let resultado = cifra
		.split('')
		.map((letra)=> {
			let code = letra.charCodeAt(0);
			code -= chave;
			if(code < 65) code += 26;
			return String.fromCharCode(code);
		})

	console.log(resultado.join(''));
}