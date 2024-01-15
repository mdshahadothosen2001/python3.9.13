class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Binary_Tree:
    def insert(self, head, data):
        if head is None:
            return TreeNode(data)
        else:
            if head.data < data:
                head.right = self.insert(head.right, data)
            else:
                head.left = self.insert(head.left, data)
        return head
    
    def pre_order_display(self, head):
        if head is not None:
            print(head.data, end=", ")
            self.pre_order_display(head.left)
            self.pre_order_display(head.right)

head = None
tree = Binary_Tree()
head = tree.insert(head, 1)
head = tree.insert(head, 2)
head = tree.insert(head, 5)
head = tree.insert(head, 4)
head = tree.insert(head, 7)
head = tree.insert(head, 9)
head = tree.insert(head, 10)
head = tree.insert(head, 8)
head = tree.insert(head, 6)
head = tree.insert(head, 11)
head = tree.insert(head, 3)
 
tree.pre_order_display(head)
