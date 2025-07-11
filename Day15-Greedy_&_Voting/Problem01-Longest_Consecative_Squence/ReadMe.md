# Longest Consecutive Sequence

## Description

This Python program finds the **length of the longest consecutive elements sequence** in an unsorted array of integers using a `set` for O(n) time complexity.

The problem is a classic application of hash-based lookups and is commonly asked in coding interviews.

## Features

- Accepts user-defined array length and elements
- Handles invalid input gracefully
- Efficient O(n) time complexity using set-based lookup
- Outputs the length of the longest consecutive subsequence

## Example

**Input:**
Enter the Length of Array = 6
Enter elements in the array:
Element 1: 100
Element 2: 4
Element 3: 200
Element 4: 1
Element 5: 3
Element 6: 2


**Output:**
Length of Longest Consecutive Sequence: 4

## How It Works

1. Input list is converted to a set for fast lookups.
2. For each number, if its previous number is not in the set, a new streak is started.
3. The streak is extended by checking consecutive elements.
4. Maximum streak length is tracked and printed.
