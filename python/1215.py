import re


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return self.value


class Tree:
    def __init__(self, root=None) -> None:
        self.root = root

    def in_order(self, node=None):
        if not node:
            node = self.root

        if node.left:
            self.in_order(node.left)

        print(node)

        if node.right:
            self.in_order(node.right)

    def add(self, node: Node, current: Node = None):
        if not current:
            current = self.root

        if not current:
            self.root = node
            return

        if node.value > current.value:
            if current.right:
                self.add(node, current.right)
            else:
                current.right = node

        elif node.value < current.value:
            if current.left:
                self.add(node, current.left)
            else:
                current.left = node


inp = ""
while 1:
    try:
        inp = inp + input() + " "
    except:
        d = {}
        root = Tree()

        def check_word(word: re.Match, dict=d):
            word: str = word.group(0)
            word = word.lower()
            if not dict.get(word):
                dict[word] = word
                root.add(Node(word))
            return ""

        re.sub(r"[a-zA-Z]+", check_word, inp)
        root.in_order()
        break
