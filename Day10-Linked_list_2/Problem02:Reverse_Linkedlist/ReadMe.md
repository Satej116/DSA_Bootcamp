# Linked List Reversal in Python

This project implements a singly linked list in Python with the ability to:
- Add elements to the rear (end) of the list
- Reverse the linked list
- Display the linked list

## Features

- **Add to Rear**: Insert a new node at the end of the linked list.
- **Reverse List**: Reverse the order of nodes in the list.
- **Display List**: Print the elements of the list in order.

## How to Use

1. **Run the Program**
python your_script_name.py

2. **Menu Options**
- `1`: Add a new integer to the end of the list.
- `2`: Reverse the list and display it.
- `3`: Exit the program.

## Sample Interaction

Choose an option:

Add to rear

Display reversed list

Exit
Enter your choice: 1
Enter value to add to rear: 10

Choose an option:

Add to rear

Display reversed list

Exit

Enter your choice: 1
Enter value to add to rear: 20

Choose an option:

Add to rear

Display reversed list

Exit
Enter your choice: 2
List reversed successfully.
20 -> 10 -> None


## Code Structure

- `ListNode`: Node class that stores data and reference to the next node.
- `MyLinkedList`: Contains methods for adding nodes, reversing the list, and printing the list.
- `while True` loop: Menu-driven interface for interacting with the list.
