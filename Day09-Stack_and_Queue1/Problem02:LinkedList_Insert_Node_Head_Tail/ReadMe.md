# Singly Linked List Implementation in Python

This project demonstrates a simple **singly linked list** data structure in Python with an interactive menu. The user can insert nodes at the front or rear of the list and display the entire list.

## Features

- **Add to Front**: Inserts a node at the beginning of the linked list.
- **Add to Rear**: Appends a node at the end of the linked list.
- **Display List**: Prints the linked list in a readable format.
- **Interactive Menu**: Repeats operations until the user chooses to exit.

## Class Structure

- **ListNode**: Represents a single node in the linked list.
  - Attributes: `data`, `next`
- **MyLinkedList**: Manages the linked list operations.
  - Methods:
    - `add_to_front(data)`
    - `add_to_rear(data)`
    - `print_list()`

## Sample Menu

Choose an option:

Add to front

Add to rear

Display list

Exit


## Example Output

Enter your choice: 1
Enter value to add to front: 10

Enter your choice: 2
Enter value to add to rear: 30

Enter your choice: 3
10 -> 30 -> None
