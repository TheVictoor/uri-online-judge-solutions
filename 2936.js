
var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
var lines = input.split( '\n' );

let [ curupira, boitata, boto, mapinguari, lara ] = lines;
let soma = 0;
let porcoes = {
  "curupira": 300,
  "boitata": 1500,
  "boto": 600,
  "mapinguari": 1000,
  "lara": 150,
  "chica": 225
};

soma += porcoes.curupira * parseInt(curupira);
soma += porcoes.boitata * parseInt(boitata);
soma += porcoes.boto * parseInt(boto);
soma += porcoes.mapinguari * parseInt(mapinguari);
soma += porcoes.lara * parseInt(lara);
soma += porcoes.chica;

console.log( soma );