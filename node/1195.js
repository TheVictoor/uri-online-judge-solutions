var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

/**
 * Escreva a sua solução aqui
 * Code your solution here
 * Escriba su solución aquí
 */


class Node {
    constructor(value) {
        this.value = value 
        this.left = null
        this.right = null
    }
}

class Tree {
    constructor() {
        this.root = null
    }

    preOrder(node, l=[]) {
        if (!node) {
            return
        }    

        l.push(node.value.toString())
        this.preOrder(node.left, l)
        this.preOrder(node.right, l)
    }

    inOrder(node, l=[]) {
        if (!node) {
            return
        }    

        this.inOrder(node.left, l)
        l.push(node.value.toString())
        this.inOrder(node.right, l)
    }

    posOrder(node, l=[]) {
        if (!node) {
            return
        }    

        this.posOrder(node.left, l)
        this.posOrder(node.right, l)
        l.push(node.value.toString())
    }

    add(root, node) {
        if (!root) {
            return node
        }

        if (node.value < root.value) {
            root.left = this.add(root.left, node)
        } else {
            root.right = this.add(root.right, node)
        }

        return root
    }
}


let nCases = parseInt(lines.shift())

for(let i = 0; i < nCases; i++) {
    let nNodes = parseInt(lines.shift())
    let nodes = lines
        .shift()
        .split(' ')
        .map(l => parseInt(l))
        .filter((v, i) => i < nNodes)
    
    let tree = new Tree()
    let firstnode = nodes.shift()
    let root = new Node(firstnode)
    tree.root = root

    nodes.forEach(node => {
        tree.add(tree.root, new Node(node))
    })

    console.log(`Case ${i+1}:`)
    let l = []
    tree.preOrder(tree.root, l)
    console.log(`Pre.: ${l.join(" ")}`)
    l = []
    tree.inOrder(tree.root, l)
    console.log(`In..: ${l.join(" ")}`)
    l = []
    tree.posOrder(tree.root, l)
    console.log(`Post: ${l.join(" ")}\n`)
}