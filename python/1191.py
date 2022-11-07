class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def pre_order(self, node=None):
        if node is None: 
            return
        
        print(node.value, end='')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node=None):
        if node is None: 
            return

        self.in_order(node.left)
        print(node.value, end='')
        self.in_order(node.right)

    def pos_order(self, node=None):
        if node is None: 
            return

        self.pos_order(node.left)
        self.pos_order(node.right)
        print(node.value, end='')


def reconstruct_tree(pre_order: list[str], in_order: list[str]):
    if len(pre_order) == 0:
        return 

    if len(pre_order) == 1:
        return Node(pre_order)

    root = Node(pre_order[0])
    pre_order = pre_order[1:]
    in_order_left, in_order_right = in_order.split(root.value)
    pre_order_left = pre_order[:len(in_order_left)]
    pre_order_right = pre_order[len(in_order_left):]
    root.left = reconstruct_tree(pre_order_left, in_order_left)
    root.right = reconstruct_tree(pre_order_right, in_order_right)
    return root


while 1:
    try:
        pre_order, in_order = input().split(" ")
        tree = Tree()
        nodes=  reconstruct_tree(pre_order, in_order)    
        tree.pos_order(nodes)
        print()
    except:
        break
