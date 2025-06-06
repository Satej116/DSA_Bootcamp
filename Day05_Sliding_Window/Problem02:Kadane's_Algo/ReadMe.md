# Sliding Window - Maximum Subarray Sum (Kadane's Algorithm)

This Python script demonstrates the use of the **sliding window technique (Kadane's Algorithm)** to find the **maximum sum of a contiguous subarray** in a user-defined array.

## Features

- Accepts dynamic user input for array length and values.
- Implements Kadane's Algorithm to find the **maximum sum of a subarray**.
- Handles input validation for non-numeric values and small array sizes.

## How It Works

1. The user is prompted to enter:
   - The length of the array (must be greater than 1).
   - The integer elements of the array.
2. The algorithm iterates through the array, maintaining two values:
   - `max_current`: Maximum subarray sum ending at the current index.
   - `max_global`: Overall maximum subarray sum found so far.
3. The program prints the original array and the maximum subarray sum.

## Sample Input/Output

Enter the Length of Array = 6
Enter elements in the array:
-2
1
-3
4
-1
2
Array = [-2, 1, -3, 4, -1, 2]
6