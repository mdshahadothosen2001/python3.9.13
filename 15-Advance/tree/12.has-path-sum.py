from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        subSum = targetSum - root.val

        if subSum == 0 and root.left is None and root.right is None:
            return True

        case = False

        if root.left is not None:
            case = case or self.hasPathSum(root.left, subSum)
        if root.right is not None:
            case = case or self.hasPathSum(root.right, subSum)

        return case

# binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

checker = Solution()
result = checker.hasPathSum(root, 4)
print(result)
