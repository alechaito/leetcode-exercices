class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(6), Node(8)))
k = 1

def kthSmallest(root, k):
    count = 0

    def inorder(node):
        nonlocal count

        if not node:
            return

        print("calling to: ", node.val)
        
        inorder(node.left)
        
        count += 1
        if count == k:
            return node.val
        else:
            inorder(node.right)
    
    r = inorder(root)

    print("nodeval", r)

print(kthSmallest(root, 1))