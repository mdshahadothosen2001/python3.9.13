class ListNode():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


list1 = ListNode(1)
list1.next = ListNode(3)

print(list1.data)
print(list1.next.data)
