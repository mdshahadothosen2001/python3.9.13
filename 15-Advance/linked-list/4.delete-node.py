# defined node as a data and address of next node
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# insert the new node to linked list
class LinkedList:
    def insert(self, head, data):
        new_node = Node(data)
        if head is None or data < head.data:
            new_node.next = head
            return new_node
        else:
            current = head
            while current.next and data >= current.next.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            return head
    def display(self, head):
        if head is None:
            print("Empty")
        else:
            current = head
            while current.next:
                print(current.data)
                current = current.next 
            print(current.data)

linked_list = LinkedList()
head = None
head = linked_list.insert(head, 5)
head = linked_list.insert(head, 2)
head = linked_list.insert(head, 4)
linked_list.display(head)

#delete node
class NewLinkedList:
    def delete(self, head, data):
            current = head
            if current is None:
                return head

            if current.data == data:
                head = current.next
                return head

            while current.next and current.next.data != data:
                current = current.next

            if current.next:
                current.next = current.next.next

            return head

# assign new linked list for delete
linked_list_1 = NewLinkedList()

#passing previous linked list as a head
linked_list_1.delete(head, 4)

#display from previous class
print("After delte node")
linked_list.display(head)
