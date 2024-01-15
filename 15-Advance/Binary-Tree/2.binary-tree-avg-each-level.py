from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        i = -1
        nodes_list = []
        nodes_level_list = []
        nodes = deque([(root, 0)])
        current_level = -1
        while nodes:
            current_node, level = nodes.popleft()
            if level > current_level:
                nodes_list.append(nodes_level_list)
                nodes_level_list = []
                current_level = level
            nodes_level_list.append(current_node.val)
            
            if current_node.left:
                nodes.append((current_node.left, level+1))
            if current_node.right:
                nodes.append((current_node.right, level+1))
        nodes_list.append(nodes_level_list)
        
        avg = []
        for node in nodes_list[1:]:
            number_of_node = len(node)
            sum_of_node = sum(node)
            div_of_node = sum_of_node / number_of_node
            avg.append(div_of_node)
        return avg

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

head.left.left = TreeNode(4)
head.left.right = TreeNode(5)



head.right.left = TreeNode(6)
head.right.right = TreeNode(7)

head.right.right.left = TreeNode(9)
head.right.right.right = TreeNode(10)

checker = Solution()
result = checker.averageOfLevels(head)
# expected : [1.0, 2.5, 5.5, 9.5]
print(result)

