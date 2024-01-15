from  typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return (
                p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)
            )

head = TreeNode(3)
head.left = TreeNode(4)
head.right = TreeNode(5)

head.left.left = TreeNode(7)
head.left.right = TreeNode(8)

head.right.left = TreeNode(10)
head.right.right = TreeNode(11)

head1 = TreeNode(1)
head1.left = TreeNode(2)

head2 = TreeNode(1)
head2.right = TreeNode(2)
root = None
checker = Solution()
result = checker.isSameTree(head1,head2)
print(result)
