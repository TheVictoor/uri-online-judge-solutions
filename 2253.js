var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let comprimento = /^.{6,32}$/;
let minusculas = /[a-z]/;
let maiusculas = /[A-Z]/;
let numeros = /[0-9]/;
let especiais = /[^a-zA-Z0-9]/;

while (true) {
	let senha = lines.shift();
	if (!senha) break;
	if(comprimento.test(senha) && minusculas.test(senha) && maiusculas.test(senha) && numeros.test(senha) && !especiais.test(senha))
		console.log('Senha valida.');
	else 
		console.log('Senha invalida.');
}