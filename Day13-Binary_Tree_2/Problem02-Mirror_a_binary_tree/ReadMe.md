# Binary Tree Mirror and Inorder Traversal

## Description

This Python program demonstrates how to perform the following operations on a binary tree:

1. **Inorder Traversal**
2. **Mirroring the Binary Tree**
3. **Inorder Traversal After Mirroring**

The tree is manually constructed, and the `mirror` function recursively swaps the left and right children of all nodes in the tree.

## Binary Tree Structure (Before Mirroring)

markdown
Copy
Edit
    1
   / \
  2   3
 / \
4   5
shell
Copy
Edit

## Inorder Traversal

Inorder traversal visits nodes in the order: **Left → Root → Right**

### Before Mirroring
Inorder output: `4 2 5 1 3`

### After Mirroring
The mirrored tree becomes:

markdown
Copy
Edit
    1
   / \
  3   2
     / \
    5   4
markdown
Copy
Edit

Inorder output after mirror: `3 1 5 2 4`
