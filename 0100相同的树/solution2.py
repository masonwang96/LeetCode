# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p and not q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


if __name__ == "__main__":
    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(3)
    y = TreeNode(1)
    y.left = TreeNode(2)
    y.right = TreeNode(3)
    print(Solution().isSameTree(x, y))
