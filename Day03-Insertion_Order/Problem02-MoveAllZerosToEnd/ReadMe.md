# Move Zeros and Sort Array

This Python script takes an integer array input from the user, moves all zeros to the end of the array, and sorts the non-zero elements in ascending order.

## Features

- Accepts user input for array length and elements.
- Moves all zero elements to the end of the array.
- Sorts the non-zero elements using Bubble Sort.
- Displays the modified array.

## How It Works

1. Prompts the user to enter the length of the array (must be greater than 1).
2. Accepts integer elements of the array.
3. Creates a new array where all non-zero elements are placed first, followed by zeros.
4. Sorts the non-zero elements in ascending order using Bubble Sort.
5. Prints the final array with zeros moved to the end.

## Sample Input/Output

Enter the Length of arr = 7
Enter elements in the arr:

0
5
3
0
2
0
1
arr = [0, 5, 3, 0, 2, 0, 1]
After modification arr = [1, 2, 3, 5, 0, 0, 0]