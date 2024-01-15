class ListNode():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new = ListNode(data)
        if self.is_empty():
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new 

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
