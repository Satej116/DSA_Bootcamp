# Binary Tree Height Calculation

## Description

This Python program defines a binary tree and calculates its height using a recursive approach.

## Features

- Constructs a binary tree manually
- Implements a recursive function to calculate the height of the binary tree
- Prints the height of the constructed binary tree

## Structure

The tree created in this program has the following structure:
    1
   / \
  2   3
 / \
4   5

## Code Overview

- `Node` class is used to create nodes of the binary tree.
- `height()` function computes the height of the tree recursively.
  - If a node is `None`, it returns `-1`.
  - Otherwise, it returns `1 + max(left_height, right_height)`.

## Output

When you run the code, it prints:

Height of the binary tree is: 2
