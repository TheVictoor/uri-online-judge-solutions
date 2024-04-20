class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self) -> None:
        self.root = None

    def add(self, root, node):
        if root is None:
            return node

        if node.value < root.value:
            root.left = self.add(root.left, node)
        elif node.value >= root.value:
            root.right = self.add(root.right, node)

        return root

    def in_level(self, root: Node, l: list):
        l.append(str(root.value))

        queue = [root.left, root.right]

        while queue:
            node = queue.pop(0)
            if node:
                l.append(str(node.value))
                queue.extend([node.left, node.right])

        return l


n_cases = int(input())

for case in range(n_cases):
    n_nodes = int(input())
    nodes = [int(n) for n in input().split(" ") if n != ""]
    # nodes = nodes[:n_nodes]
    tree = Tree()

    n_nodes -= 1
    tree.root = Node(nodes.pop(0))

    for node in nodes:
        n = Node(node)
        tree.add(tree.root, n)

    print(f"Case {case+1}:")
    l = []
    tree.in_level(tree.root, l)
    print(" ".join(l))
    print()
