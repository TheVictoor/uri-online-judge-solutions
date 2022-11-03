

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self) -> None:
        self.root = None

    def pre_order(self, node=None, l=[]):
        if node is None: 
            return
        
        l.append(str(node.value))
        self.pre_order(node.left, l)
        self.pre_order(node.right, l)

    def in_order(self, node=None, l=[]):
        if node is None: 
            return

        self.in_order(node.left, l)
        l.append(str(node.value))
        self.in_order(node.right, l)

    def pos_order(self, node=None, l=[]):
        if node is None: 
            return

        self.pos_order(node.left, l)
        self.pos_order(node.right, l)
        l.append(str(node.value))

    def add(self, root, node):
        if root is None:
            return node

        if node.value < root.value:
            root.left = self.add(root.left, node)
        elif node.value >= root.value:
            root.right = self.add(root.right, node)
        
        return root


n_cases = int(input())

for case in range(n_cases):
    n_nodes = int(input())
    nodes = [int(n) for n in input().split(" ") if n != ""]
    # nodes = nodes[:n_nodes]
    tree = Tree()

    n_nodes -= 1
    tree.root = Node(nodes.pop(0))

    for index, node in enumerate(nodes):
        if index >= n_nodes - 1:
            continue
        n = Node(node)
        tree.add(tree.root, n)

    print(f"Case {case+1}:")
    l = []
    tree.pre_order(tree.root, l)
    print('Pre.: {0}'.format(" ".join(l)))
    l = []
    tree.in_order(tree.root, l)
    print('In..: {0}'.format(" ".join(l)))
    l = []
    tree.pos_order(tree.root,l)
    print('Post: {0}'.format(" ".join(l)))
    print('')
