__author__ = 'shehryar'

class BST():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node):
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


    def search(self,node, parent=None):
        if node <self.data:
            if self.left is None:
                return None
            return self.left.search(node,self)
        elif node > self.data:
            if self.right is None:
                return None
            return self.right.search(node,self)
        else:
            return self,parent

    def delete(self, node, parent = None):
        if self.data:
            if node < self.data:
                if self.left is None:
                    return None

    def all_nodes(self):
        visited = []
        if self:
            if self.left:
                self.left.all_nodes()
            visited.append(self.data)
            if self.right:
                self.right.all_nodes()








tree = BST(6)
tree.insert(4)