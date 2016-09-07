
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
        self.first = None

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

    def reverse(self):
        original_first = self.first
        current = self.first
        previous = None
        i = 0
        while current:
            i += 1
            if current == original_first:
                # If we are on the first node
                if not current.next_node:
                    # End early if not a 2nd node.
                    break
                else:
                    previous = current
                    current = current.get_next()
                    continue
            if i == 2: # 1 based instead of the usual 0
                previous.next_node = None
            original_next_node = current.get_next()
            current.next_node = previous
            if original_next_node:
                previous = current
                current = original_next_node
            else:
                self.first = current
                current = None


if __name__ == "__main__":
    LL = LinkedList()
    LL.insert(Node("a"))
    LL.insert(Node("b"))
    # LL.insert(Node("c"))

    pointer = LL.first
    while pointer:
        print "Current value: {}".format(pointer.data)
        pointer = pointer.get_next()

    LL.reverse()
    print "Reversed!"

    pointer = LL.first
    while pointer:
        print "Current value: {}".format(pointer.data)
        pointer = pointer.get_next()
