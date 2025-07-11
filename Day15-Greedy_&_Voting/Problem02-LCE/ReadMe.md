# Lowest Common Ancestor (LCA) in Binary Tree

## Description

This Python program demonstrates how to find the **Lowest Common Ancestor (LCA)** of two nodes in a binary tree. The LCA of two nodes `p` and `q` is defined as the lowest node in the tree that has both `p` and `q` as descendants (where a node can be a descendant of itself).

The algorithm uses recursion and works for a general binary tree (not necessarily a binary search tree).

## Features

- Builds a custom binary tree.
- Implements a recursive function to find the LCA of two nodes.
- Outputs the LCA node's value.

## Tree Structure

The tree used in this example:

markdown

    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4


## Example Output

LCA of 5 and 1: 3
LCA of 5 and 4: 5


## How It Works

- **`TreeNode`**: A class that represents a node in the binary tree.
- **`BinaryTree`**: A class that initializes the root and contains a static method `find_lca`.
- **`find_lca(root, p, q)`**: 
  - Returns `root` if it matches either `p` or `q`.
  - Recursively searches for `p` and `q` in left and right subtrees.
  - If both subtrees return non-null, the current node is the LCA.
