# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        #left < value < right
        def search(node, left, right):
            if not node:
                return True
            
            if not (node.val > left and node.val < right):
                return False
            
            # update boundaries to guarantee that is a valid binary tree
            return search(node.left, left, node.val) and search(node.right, node.val, right)

        # start without any restriction because its root
        return search(root, float("-inf"), float("inf"))

            
