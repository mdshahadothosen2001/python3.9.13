from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_display(head):
    if head is not None:
        print(head.data, end=", ")
        pre_order_display(head.left)
        pre_order_display(head.right)

def in_order_display(head):
    if head is not None:
        in_order_display(head.left)
        print(head.data, end=", ")
        in_order_display(head.right)

def post_order_display(head):
    if head is not None:
        post_order_display(head.left)
        post_order_display(head.right)
        print(head.data, end=", ")

def display_level_order_with_levels(root):
    if root is None:
        return

    queue = deque([(root, 0)]) 

    current_level = -1

    while queue:
        current_node, level = queue.popleft()

        if level > current_level:
            print("\nLevel", level + 1, ":", end=" ")
            current_level = level

        print(current_node.data, end=" ")

        if current_node.left:
            queue.append((current_node.left, level + 1))
        if current_node.right:
            queue.append((current_node.right, level + 1))

def display_level_order_with_depth(root):
    if root is None:
        return

    queue = deque([(root, 0)])

    while queue:
        current_node, depth = queue.popleft()

        print(f"Node: {current_node.data}, Depth: {depth}")

        if current_node.left:
            queue.append((current_node.left, depth + 1))
        if current_node.right:
            queue.append((current_node.right, depth + 1))


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

head.left.left = TreeNode(4)
head.left.right = TreeNode(5)

head.left.right.left = TreeNode(8)



head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

head.right.right.left = TreeNode(9)
head.right.right.right = TreeNode(10)

root = head
print("Pre oder : ", end="")
pre_order_display(root)

root = head
print("\nIn oder : ", end="")
in_order_display(root)

root = head
print("\nPost oder : ", end="")
post_order_display(root)

root = head
print("\n\nLevel order with levels: ", end="")
display_level_order_with_levels(root)

root = head
print("\n\nLevel order with dept : ")
display_level_order_with_depth(root)



            #                  1
            #                 / \
            #                /   \
            #               /     \
            #              /       \
            #             /         \
            #            /           \
            #           /             \
            #          /               \
            #        2                  3
            #       / \                / \
            #      /   \              /   \
            #     /     \            /     \
            #    4       5          6       7
            #           /                  /  \
            #          /                  /    \
            #         /                  /      \
            #        8                  9        10

# pre order   : 1, 2, 4, 5, 8, 3, 6, 7, 9,
# In order    : 4, 2, 8, 5, 1, 6, 3, 9, 7, 10 
# post order  : 4, 8, 5, 2, 6, 9, 10, 7, 3, 1
