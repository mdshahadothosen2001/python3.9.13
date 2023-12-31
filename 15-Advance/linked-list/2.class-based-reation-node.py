# defined node as a data and address of next node
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Linked list operations
class LinkedList():
    # initially set head = None
    def __init__(self) -> None:
        self.head = None
    
    # check head is none or set value
    def is_empty(self):
        return self.head is None
    
    # create new node
    def append(self, data):
        new = Node(data)
        if self.is_empty():
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new 
    # display node list means linked list
    def display(self):
        if self.is_empty():
            print("Empty")
        else:
            current = self.head
            while current.next:
                print("Node is", current.data)
                current = current.next 
            print("Node is", current.data)

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()