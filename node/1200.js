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

    search(root, value) {
        if (!root) {
            return false
        }

        if (value === root.value) {
            return true
        } else if (value < root.value) {
            return this.search(root.left, value)
        } else if (value > root.value) {
            return this.search(root.right, value)
        }
    }

    remove(root, value) {
        if (!root) {
            return false
        }

        if (value < root.value) {
            root.left =  this.remove(root.left, value)
        } else if (value > root.value) {
            root.right = this.remove(root.right, value)
        } else {
            if (!root.left) {
                return root.right
            } else if (!root.right) {
                return root.left
            }

            root.value = this.maxValue(root.left)
            root.left = this.remove(root.left, root.value)
        }

        return root
    }

    maxValue(root) {
        let maxv = root.value;
        while (root.right) {
            maxv = root.right.value;
            root = root.right;
        }
        return maxv;
    }
}


let tree = new Tree()


while (lines.length) {
    let [op, value] = lines.shift().split(' ')

    if (op === "I") {
        let n = new Node(value)
        tree.root = tree.add(tree.root, n)
    } else if (op == "P") {
        let r = tree.search(tree.root, value)
        console.log(!!r ? `${value} existe` : `${value} nao existe`)
    } else if (op == "R") {
        tree.root = tree.remove(tree.root, value)
    } else if (op == "INFIXA") {
        let l = []
        tree.inOrder(tree.root, l)
        console.log(l.join(" "))
    } else if (op == "POSFIXA") {
        let l = []
        tree.posOrder(tree.root, l)
        console.log(l.join(" "))
    } else if (op == "PREFIXA") {
        let l = []
        tree.preOrder(tree.root, l)
        console.log(l.join(" "))
    }
}