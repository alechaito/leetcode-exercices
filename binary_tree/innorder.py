class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)
    return result

root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6), Node(8)))
print(inorderTraversal(root)) # Output: [2, 3, 4, 5, 6, 7, 8]