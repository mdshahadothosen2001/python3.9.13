class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root
    
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.data = find_min_value_node(root.right).data
        root.right = delete_node(root.right, root.data)
    return root

def display_inorder(root):
    if root is not None:
        display_inorder(root.left)
        print(root.data, end=" ")
        display_inorder(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


print("Original Tree : ")
display_inorder(root)
print()

key_to_delete = 8
root = delete_node(root, key_to_delete)

print("After deletion: ")
display_inorder(root)
