# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def dfs(current_node, current_sum):
            if not current_node:
                return False

            current_sum += current_node.val
            if (current_sum == targetSum 
                and not current_node.left
                and not current_node.right
            ):
                return current_sum == targetSum 

            return (
                dfs(current_node.left, current_sum) 
                or dfs(current_node.right, current_sum)
            )

        return  dfs(root, 0)

"""
Base case: 

1 - check sum
2 - check if is a left

call (1, 2) step to left side
call (1, 2) step to right side

"""