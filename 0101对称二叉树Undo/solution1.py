# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.right and not root.left:
            return True
        elif root.right and root.left and root.right.val == root.left.val:
            return self.isSymmetric(root.right) and self.isSymmetric(root.left)
        else:
            return False


if __name__ == "__main__":
    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(2)
    x.left.left = TreeNode(3)
    x.left.right = TreeNode(4)
    x.right.left = TreeNode(4)
    x.right.right = TreeNode(3)
    print(Solution().isSymmetric(x))
