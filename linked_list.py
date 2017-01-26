__author__ = 'shehryar'

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node

        else:
            node.next = self.head
            node.next.prev = node
            self.head = node



    def search(self, key):
        node = self.head
        if node != None:
            while node.next != None:
                if (node.data == key):
                    return node
                node = node.next
            if (node.data == key):
                return node

        return None

    def remove(self, key):
        pre = key.prev
        key.prev.next = key.next
        key.prev = pre


    def print_list(key):
        nodelist = []
        while key:
            nodelist.append(key.data)
            key = key.next

