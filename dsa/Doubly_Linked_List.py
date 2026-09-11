class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    
    # Print the list to produce output
    curr = dll.head
    elements = []
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(elements))