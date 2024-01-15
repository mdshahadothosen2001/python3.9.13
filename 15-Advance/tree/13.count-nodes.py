from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        number_of_nodes = 0
        if root is None:
            return number_of_nodes
        
        root_deque = deque([root])
        while root_deque:
            current_node = root_deque.popleft()
            number_of_nodes += 1 
            if current_node.left:
                root_deque.append(current_node.left)
            if current_node.right:
                root_deque.append(current_node.right)
        return number_of_nodes


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

checker = Solution()
result = checker.countNodes(root)
print(result)
