class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    res = []
    if root:
        res.extend(inorder(root.left))
        res.append(root.val)
        res.extend(inorder(root.right))
    return res

# Driver execution
vals = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93, 3, 9, 15, 21, 28, 34, 40, 46, 53, 59]
root = None
for v in vals:
    root = insert(root, v)

print("Sorted In-Order Traversal:")
print(inorder(root))