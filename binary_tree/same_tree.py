# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(p, q):
            if not p and not q:
                return True
            if q and p and q.val == p.val:
                return bfs(p.left, q.left) and bfs(p.right, q.right)
            else:
                return False
        
        same = bfs(p, q)


        return same


"""
    Until we have the same value on the root we keep going recursively,
    we can reach the end of the tree with all values equal that show its equal
    or we can find a root that is different and it will return False
"""