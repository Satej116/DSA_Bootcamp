# Linked List Operations in Python

## Description

This Python program implements a singly linked list that supports the following operations:

- Adding nodes to the rear of the list
- Reversing the linked list
- Displaying elements up to a specific value
- Simulated cycle detection based on a given value (not a memory reference cycle)

## Features

- Custom implementation of `ListNode` and `MyLinkedList` classes
- Reversal of the linked list using iterative method
- Controlled display of nodes up to a target value
- Simple simulation to check if a value exists in the list to mimic cycle detection logic

## Menu Options

1. Add to rear  
   - Appends a new node to the end of the linked list.

2. Reverse and display list  
   - Reverses the linked list.
   - Displays elements up to a user-specified value.
   - Checks whether the given value was present in the list to simulate cycle detection.

3. Exit  
   - Ends the program.

## How to Use

1. Run the program.
2. Choose option `1` to insert elements at the end.
3. Choose option `2` to reverse the list and display it until a specific element is encountered.
4. Based on whether that element exists in the list, the program prints `True` (simulating a "cycle") or `False`.
5. Use option `3` to exit.

## Sample Output

Choose an option:

Add to rear

Reverse and display list

Exit
Enter your choice: 1
Enter value to add to rear: 10

Choose an option:

Add to rear

Reverse and display list

Exit
Enter your choice: 1
Enter value to add to rear: 20

Choose an option:

Add to rear

Reverse and display list

Exit
Enter your choice: 2
Enter the element to which you have to traverse: 10
List reversed successfully.
Current List:
20 -> 10 ->
True