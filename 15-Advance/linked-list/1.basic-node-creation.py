# Defined node as a two part data and address of next node
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# assign nodes
list1 = Node(1)
list1.next = Node(3)

# access node and display
print(list1.data)
print(list1.next.data)
