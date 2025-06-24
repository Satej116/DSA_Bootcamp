# Binary Tree Traversal in Python

## Description

This Python program demonstrates how to perform the three main types of depth-first traversals on a binary tree:

- **Preorder Traversal**
- **Inorder Traversal**
- **Postorder Traversal**

The program uses a simple class-based approach to define nodes in the binary tree and then implements recursive functions to traverse the tree in each of the three orders.

## Binary Tree Structure

The tree constructed in the code looks like this:

    1
   / \
  2   3
 / \
4   5

## Traversal Methods

1. **Preorder (Root → Left → Right)**  
   Output: `1 2 4 5 3`

2. **Inorder (Left → Root → Right)**  
   Output: `4 2 5 1 3`

3. **Postorder (Left → Right → Root)**  
   Output: `4 5 2 3 1`