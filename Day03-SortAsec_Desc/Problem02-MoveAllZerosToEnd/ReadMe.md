# Bubble Sort and Move Zeros to End

## Description

This Python program:

- Takes input from the user to create an integer array.
- Sorts the array in ascending order using the Bubble Sort algorithm.
- Moves all zeros in the sorted array to the end while maintaining the order of non-zero elements.

## How It Works

1. User inputs the length of the array (must be greater than 1).
2. User inputs array elements (only numerical values allowed).
3. The array is sorted using Bubble Sort.
4. All zeros in the array are shifted to the end.

## Sample Input & Output

**Input:**
Enter the Length of Array = 6
Enter elements in the array:
3
0
1
0
2
4

makefile
Copy
Edit

**Output:**
Array= [0, 0, 1, 2, 3, 4]
Array= [1, 2, 3, 4, 0, 0]

shell
Copy
Edit

## Time Complexity

- Bubble Sort: O(n²)

## Usage

Run the script and follow the prompts:

```bash
python bubble_sort_move_zeros.py