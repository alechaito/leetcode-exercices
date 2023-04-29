# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    print(f"root: {root.val}")
    mid = inorder.index(preorder[0])
    print(f"mid: {mid}")
    print(f"preorder: {preorder}")
    print(f"inorder: {inorder}")

    root.left = buildTree(preorder[1 : mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

    return root

buildTree(preorder, inorder)

"""
1 - preorder list will give us the roots of the subtress
2 - root value is always the first element of preorder list
3 - with that we can take the middle of the inorder list based on the value of that root
4 - to the left portion we now that everything to the left from the middle point is going to be from the left
5 - to the right portion we now that everything to the right....

"""