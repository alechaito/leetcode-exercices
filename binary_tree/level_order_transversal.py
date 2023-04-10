# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        queue = collections.deque()

        if root:
            queue.append(root)
        
        # iterate until the queue is empty
        while queue:
            lvl = []
            # this will make sure that we are iterating just over the elements that was already there
            queueLen = len(queue)
            for i in range(queueLen):
                node = queue.popleft() # [3, 4, 5] <- will remove element 5
                if node:
                    lvl.append(node.val)
                    # add sons of the node to queue
                    queue.append(node.left)
                    queue.append(node.right)
            
            if lvl:
                result.append(lvl)
        
        return result