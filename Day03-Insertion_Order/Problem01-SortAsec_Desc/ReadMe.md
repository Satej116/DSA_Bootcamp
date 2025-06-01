# Array Sorting: Ascending and Descending Order

## Overview

This Python program sorts user-input array values in **ascending** and **descending** order. It uses the **Selection Sort** algorithm for ascending sorting and then reverses the sorted array to get descending order.

## Features

- Accepts array length and elements from user input
- Validates input for numeric correctness and positive array length
- Sorts array in both ascending and descending order

## Example

**Input:**
Enter the Length of Array = 5
Enter elements in the array:
10
3
7
4
2

makefile
Copy
Edit

**Output:**
Array = [10, 3, 7, 4, 2]
Ascending Sorted Array = [2, 3, 4, 7, 10]
Descending Sorted Array = [10, 7, 4, 3, 2]

markdown
Copy
Edit

## Time & Space Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n) (due to additional array for descending order)

## Note

- Best suited for small datasets and learning sorting basics.