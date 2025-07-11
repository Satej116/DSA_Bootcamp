# Majority Element Finder (Boyer-Moore Voting Algorithm)

## Description

This Python script identifies the majority element in a list using the **Boyer-Moore Voting Algorithm**, which is an efficient linear-time algorithm that uses constant space.

A **majority element** is an element that appears more than ⌊n / 2⌋ times in an array of size `n`.

## Features

- Takes user input for the size and elements of the array.
- Uses a space-optimized approach to determine the majority element.
- Handles non-numeric and invalid inputs gracefully.

## How It Works

1. `GetData()` function collects integer inputs from the user.
2. `maj_Element(nums)` applies the Boyer-Moore Voting Algorithm to find the majority element.
3. The result is printed to the console.

## Sample Output

Enter the Length of Array = 5
Enter elements in the array:
Element 1: 3
Element 2: 3
Element 3: 4
Element 4: 2
Element 5: 3
Array = [3, 3, 4, 2, 3]

Majority Element is: 3
