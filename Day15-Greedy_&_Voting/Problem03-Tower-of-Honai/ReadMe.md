# Tower of Hanoi Solver

## Description

This Python program solves the **Tower of Hanoi** problem using a recursive approach. It prints the sequence of moves required to shift all disks from the source rod to the destination rod, following the classic rules of the puzzle:

1. Only one disk can be moved at a time.
2. Each move involves taking the upper disk from one of the stacks and placing it on top of another stack.
3. No larger disk may be placed on top of a smaller disk.

## Features

- Recursive solution to the Tower of Hanoi problem
- Displays each move in a human-readable format
- Counts and displays the total number of moves
- Handles multiple test cases
- Handles edge case when `n <= 0`

## Example

**Input:**
n = 3

**Output:**
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
Total moves: 7