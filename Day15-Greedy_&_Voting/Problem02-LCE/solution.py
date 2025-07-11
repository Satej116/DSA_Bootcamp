class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    
    def find_lca(root, p, q):
        
        if root is None or root.data == p or root.data == q:
            return root

        left_lca = BinaryTree.find_lca(root.left, p, q)
        right_lca = BinaryTree.find_lca(root.right, p, q)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca else right_lca


tree = BinaryTree()
tree.root = TreeNode(3)
tree.root.left = TreeNode(5)
tree.root.right = TreeNode(1)
tree.root.left.left = TreeNode(6)
tree.root.left.right = TreeNode(2)
tree.root.right.left = TreeNode(0)
tree.root.right.right = TreeNode(8)
tree.root.left.right.left = TreeNode(7)
tree.root.left.right.right = TreeNode(4)


lca_node1 = BinaryTree.find_lca(tree.root, 5, 1)
lca_node2 = BinaryTree.find_lca(tree.root, 5, 4)

print(f"LCA of 5 and 1: {lca_node1.data if lca_node1 else 'Not found'}")
print(f"LCA of 5 and 4: {lca_node2.data if lca_node2 else 'Not found'}")
