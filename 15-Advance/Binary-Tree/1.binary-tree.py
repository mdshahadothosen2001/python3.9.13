class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def InsertNode(self, root, key):
        if root is None:
            return TreeNode(key)
        if key< root.val:
            root.left = self.InsertNode(root.left, key)
        elif key>root.val:
            root.right = self.InsertNode(root.right, key)
        return root
    
    def PreOrderTraversal(self, root):
        if root:
            print(root.val, end=", ")
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)

root = TreeNode(50)

checker = Solution()

root = checker.InsertNode(root, 20)
root = checker.InsertNode(root, 60)
root = checker.InsertNode(root, 10)
checker.PreOrderTraversal(root)
