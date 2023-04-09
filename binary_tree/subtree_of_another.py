# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False

        def sameTree(p, q):
            if not p and not q:
                return True
            if q and p and q.val == p.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            else:
                return False

        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


"""
    1 - Pay attention to edge cases
    2 - Check always if have the same tree on the current root and subroot
    3 - If not recursively call to left and right mantaining the same subroot

"""