// var input = require( 'fs' ).readFileSync( '/dev/stdin', 'utf8' );
// var lines = input.split( '\n' );

// [ [ 45, 8, 3, 1 ]
// 	, [ 1, 10, 5, 67 ]
// 	, [ 4, 4, 3, 18 ]
// 	, [ 10, 4, 7, 12 ] ]

let vet = [ [ 45, 08, 03, 01 ]
	, [ 01, 10, 05, 67 ]
	, [ 04, 04, 03, 18 ]
	, [ 10, 04, 07, 12 ] ];

// vet = [ [ 5, 2, 4 ], [ 3, 6, 7 ], [ 10, 5, 10 ] ];

// vet = [[10, 9, 8, 7, 99, 5, 1, 15, 7]
// 		,[25, 31, 33, 1, 54, 87, 5, 12, 3]
// 		,[9, 9, 1, 60, 14, 23, 47, 2, 3]
// 		,[5, 21, 15, 31, 1, 47, 21, 9, 90]
// 		,[91, 5, 10, 5, 16, 59, 40, 8, 87]
// 		,[67, 4, 80, 7, 17, 50, 47, 9, 15]
// 		,[13, 16, 12, 10, 8, 1, 3, 47, 23]
// 		,[14, 99, 21, 5, 23, 1, 21, 6, 1]
// 		,[6, 47, 12, 10, 24, 4, 5, 12, 99]];

let removeByLine = [];
let vetPossiveis = new Set();

// set the number of items for to remove in the line of the matriz
// the line is represented here by index
function setRemovedByLine() {
	for ( let i = 0; i < vet.length; i++ ) {
		removeByLine.push( vet.length - ( i + 1 ) );
	}
}

// to perform a validation over the matriz to see if 
// is valid following the rules of the problem resolution
function validarMatriz( vet ) {
	return checkHorizontal( vet );
}

function checkHorizontal( matriz ) {
	
	for ( let i = 0; i < matriz.length; i++ ) {
		for ( let j = 0; j < matriz.length; j++ ) {
			if ( matriz[ i ][ j ] != 0 ) {
				if ( !checkVertical( matriz, i, j ) ) {
					return false;
				}
			}
		}
	}

	return true;
}

function checkVertical( matriz, line = 0, column = 0 ) {
	// console.log("vertical");
	for ( let i = line; i < matriz.length; i++ )
		if ( matriz[ i ][ column ] == 0 )
			return false;
	return true;
}

// sum the values of the matriz
function countMatriz( matriz ) {
	let count = 0;

	for ( let i = 0; i < matriz.length; i++ )
		for ( let j = 0; j < matriz[ i ].length; j++ )
			count += matriz[ i ][ j ];

	console.log(matriz  , count);
	vetPossiveis.add( count );
}

// build a full tree of the values for all possibilies of matriz 
// based in your rules
// the values that need be excluded are setted to 0
function buildTree( sizeMatriz, line, nItensRemove, matriz = [] ) {

	// if there is no item to remove now 
	// then we need go for the next line 
	// and to discover the number of items that need
	// be removed 
	if ( nItensRemove == 0 ) {
		line++;
		nItensRemove = removeByLine[ line ] || 0;
	}

	// check if it's the end 
	// if is the last line e there is no item to be removed 
	// then make a validation over the matriz to see if is in a valid composition
	if ( ( line + 1 ) == sizeMatriz && nItensRemove == 0 ) {
		let valid = validarMatriz( matriz );
		if ( valid ) {
			countMatriz( matriz );
		}
		return;
	} else {

		// else remove a item from current line of matriz e execute 
		// a build of tree based in the current state of the matriz 
		// obs:
		// its is executed for each item in the line e then solicited a new tree based based in there state
		// its a recursive function to build a full tree of possibilities
		for ( let i = 0; i < matriz[ line ].length; i++ ) {

			// check if the current item in the line is not excluded yet
			if ( matriz[ line ][ i ] != 0 ) {

				// copy the matriz to contiue a build the tree without change the original matriz
				let vetaux = [];
				for ( v of matriz ) {
					vetaux.push( [ ...v ] );
				}
				vetaux[ line ][ i ] = 0;
				buildTree( sizeMatriz, line, nItensRemove - 1, vetaux );
			}
		}

	}

}

setRemovedByLine();
buildTree( vet.length, 0, removeByLine[ 0 ], [ ...vet ] );

console.log( "arvore concluida" );
vetPossiveis = [ ...vetPossiveis ].sort( ( a, b ) => a - b );
console.log( vetPossiveis[ 0 ] );