#    Main Author(s): Dev Soni
#    Main Reviewer(s): Sarah Haque

class DoublyLinked:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data is not None:
            self.head = self.Node(data)
            self.tail = self.head

    def get_front(self):
        return self.head

    def get_back(self):
        return self.tail

    def push_front(self, data):
        nn = self.Node(data, next=self.head)
        if self.head is None:
            self.tail = nn
        else:
            self.head.prev = nn
        self.head = nn

    def push_back(self, data):
        nn = self.Node(data, prev=self.tail)
        if self.tail is None:
            self.head = nn
        else:
            self.tail.next = nn
        self.tail = nn

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty list')
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty list')
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return data

    def is_empty(self):
        return self.head is None

    def insert_after(self, data, node):
        if node is None:
            self.push_front(data)
        else:
            nn = self.Node(data, next=node.get_next(), prev=node)
            if node.get_next() is not None:
                node.get_next().prev = nn
            node.next = nn
            if node == self.tail:
                self.tail = nn

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.get_next()
        return None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def is_palindrome(self):
        # Recursive additional function to check if two nodes are same
        def nodes_are_equal(node1, node2):
            if node1 is None or node2 is None:
                return True  # Both nodes are None (end of the list)
            return node1.get_data() == node2.get_data() and nodes_are_equal(node1.get_next(), node2.get_previous())

        return nodes_are_equal(self.head, self.tail)
