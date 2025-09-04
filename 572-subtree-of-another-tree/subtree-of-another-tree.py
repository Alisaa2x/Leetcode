# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: check if root / subroot is empty
        if subRoot is None:
            return True
        if root is None:
            return False

        # check if the two trees are the same starting at this node
        if self.isSameTree(root, subRoot):
            return True
        # else keep searching in the left and right children
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    # helper class to see if the two trees are the same
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if roots are empty
        if p == None and q == None:
            return True
        if (p == None and q) or (q == None and p):
            return False
        # check if val at root are the same
        if p.val != q.val:
            return False
        # check left & right to see if values are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)