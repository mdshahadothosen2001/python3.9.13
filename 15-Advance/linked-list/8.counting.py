class ListNode():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def insert(self, head, data):
        new_node = ListNode(data)
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
    def count(self, head):
        current = head
        count = 1
        while current.next:
            count += 1
            current = current.next 
        print("count ", count)        

linked_list = LinkedList()
head = None

linked_list.display(head)

head = linked_list.insert(head, 5)
head = linked_list.insert(head, 2)
head = linked_list.insert(head, 4)
linked_list.display(head)
linked_list.count(head)

