class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sorted_bst_to_avl(root):
    if not root:
        return None

    sorted_nodes = []
    in_order_traversal(root, sorted_nodes)
    return build_avl_tree(sorted_nodes)


def in_order_traversal(node, result):
    if node:
        in_order_traversal(node.left, result)
        result.append(node)
        in_order_traversal(node.right, result)

def build_avl_tree(sorted_nodes):
    if not sorted_nodes:
        return None

    mid = len(sorted_nodes) // 2
    root = sorted_nodes[mid]

    root.left = build_avl_tree(sorted_nodes[:mid])
    root.right = build_avl_tree(sorted_nodes[mid + 1:])

    return root


def pre_order_traversal(root):
    if root:
        print(root.key, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


bst_root = TreeNode(5)
bst_root.left = TreeNode(10)
bst_root.right = TreeNode(20)
bst_root.right.left = TreeNode(25)
bst_root.right.right = TreeNode(30)

print("Original BST:")
pre_order_traversal(bst_root)

avl_root = sorted_bst_to_avl(bst_root)

print("\nConverted AVL:")
pre_order_traversal(avl_root)
