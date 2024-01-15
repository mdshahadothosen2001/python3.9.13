class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_mirror_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return (root1.value == root2.value) and \
           are_mirror_trees(root1.left, root2.right) and \
           are_mirror_trees(root1.right, root2.left)

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)

tree2 = TreeNode(1)
tree2.left = TreeNode(3)
tree2.right = TreeNode(2)
tree2.right.left = TreeNode(5)
tree2.right.right = TreeNode(4)

# Check if the trees are mirrors
result = are_mirror_trees(tree1, tree2)
print(result)
