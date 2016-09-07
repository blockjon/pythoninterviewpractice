
class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        if self.head:
            self.head.next_node = node
        else:
            self.first = node
        self.head = node

    def size(self):
        current = self.first
        if not current:
            return 0
        nodes = 1
        while current.next_node:
            current = current.next_node
            nodes += 1
        return nodes

    def search(self, value):
        current = self.first
        i = 0
        while current:
            if current.data == value:
                return i
            current = current.get_next()
            i += 1
        raise ValueError("{} not found in list".format(value))

    def delete(self, value):
        current = self.first
        previous = None
        while current:
            if current.data == value:
                if previous:
                    if current.get_next():
                        previous.next_node = current.get_next()
                    else:
                        previous.next_node = None
                else:
                    if current.get_next():
                        self.first = current.get_next()
                    else:
                        self.first = None
                return
            else:
                previous = current
                current = current.get_next()


if __name__ == "__main__":
    LL = LinkedList()
    LL.insert(Node("a"))
    LL.insert(Node("b"))
    LL.insert(Node("c"))
    print "linked list size is {}".format(LL.size())
    print LL.delete("b")
    print "linked list size is {}".format(LL.size())

    pointer = LL.first
    while pointer:
        print "Current value: {}".format(pointer.data)
        pointer = pointer.get_next()
