class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def insert_node(self, head, data):
        if head is None:
            return TreeNode(data)

        if data < head.data:
            head.left = self.insert_node(head.left, data)
        elif data > head.data:
            head.right = self.insert_node(head.right, data)

        return head

    def pre_order_display(self, head):
        if head is not None:
            print(head.data, end=", ")
            self.pre_order_display(head.left)
            self.pre_order_display(head.right)

head = TreeNode(5)

tree = Tree()
print("Before insert: ")
tree.pre_order_display(head)
head = tree.insert_node(head, 3)
head = tree.insert_node(head, 7)
head = tree.insert_node(head, 2)
head = tree.insert_node(head, 4)
head = tree.insert_node(head, 6)
head = tree.insert_node(head, 8)
print("\nAfter insert: ")
tree.pre_order_display(head)
