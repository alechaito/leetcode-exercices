class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    result = []

    def preorder(node):
        if not node:
            return

        result.append(node.val)

        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return result

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(preorderTraversal(root))