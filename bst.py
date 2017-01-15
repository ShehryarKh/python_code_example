__author__ = 'shehryar'

class BST():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node):
        print(type(self.left))
        if self.data:
            if node < self.data:
                if self.left is None:
                    self.left = BST(node)
                else:
                    self.left.insert(node)
            elif node > self.data:
                if self.right is None:
                    self.right = BST(node)
                else:
                    self.right.insert(node)
        else:
            self.data = node



tree = BST(6)
tree.insert(4)