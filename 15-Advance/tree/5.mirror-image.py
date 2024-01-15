from  collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_mirror_tree(head):
    if head is None:
        return None
    head.left, head.right = head.right, head.left

    create_mirror_tree(head.left)
    create_mirror_tree(head.right)

    return head

def display_level_order_with_depth(head):
    if head is None:
        return

    queue = deque([(head, 0)])

    while queue:
        current_node, depth = queue.popleft()

        print("Node ", current_node.data, " Depth: ", depth)

        if current_node.left:
            queue.append((current_node.left, depth + 1))
        if current_node.right:
            queue.append((current_node.right, depth + 1))


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

head.left.left = TreeNode(4)
head.left.right = TreeNode(5)

head.right.left = TreeNode(6)
head.right.right = TreeNode(7)


print("Original Tree:")
display_level_order_with_depth(head)


mirror_head = create_mirror_tree(head)


print("\nMirror Image:")
display_level_order_with_depth(mirror_head)
