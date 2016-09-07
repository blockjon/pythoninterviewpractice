

class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.data == data:
            return False
        if data < self.data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def find(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if data.left_child:
                return data.left_child.find(data)
            else:
                return False
        if data > self.data:
            if self.right_child:
                return self.right_child.find(data)
            else:
                return False


class Tree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False


if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(8)
    tree.insert(9)
    tree.insert(7)
    assert tree.find(9)
    assert not tree.find(12)
