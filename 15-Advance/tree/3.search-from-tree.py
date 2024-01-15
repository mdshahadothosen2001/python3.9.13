class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_node(head, target):
    if head is None or head.data == target:
        return head
    
    left_result = search_node(head.left, target)
    if left_result:
        return left_result

    return search_node(head.right, target)

head = TreeNode(5)
head.left = TreeNode(3)
head.right = TreeNode(7)

head.left.left = TreeNode(2)
head.left.right = TreeNode(4)

head.right.left = TreeNode(6)
head.right.right = TreeNode(8)


target_value = 46
result = search_node(head, target_value)
if result is not None:
    print("Founded data")
else:
    print("Not found")
