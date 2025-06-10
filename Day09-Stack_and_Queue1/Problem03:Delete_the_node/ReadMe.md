# Singly Linked List in Python (with Delete Functionality)

This project is a Python implementation of a **singly linked list** that supports interactive operations like appending to the rear, deleting a node by value, and displaying the list.

## Features

- **Add to Rear**: Appends a new node to the end of the linked list.
- **Delete Node**: Deletes the first node found with the given value.
- **Display List**: Prints all the elements of the linked list.
- **Interactive Menu**: Allows users to perform multiple operations via a loop.

## Class Definitions

### `ListNode`
Represents a node in the linked list.

- `data`: Stores the value.
- `next`: Points to the next node.

### `MyLinkedList`
Contains the logic for managing the linked list.

- `add_to_rear(data)`: Adds a new node at the end.
- `delete_node(data)`: Deletes the first occurrence of a node with the given value.
- `print_list()`: Displays the current list in readable format.

## Example Menu

Choose an option:

Delete node

Add value at tail

Display list

Exit

shell
Copy
Edit

## Sample Output

Enter your choice: 2
Enter value to add to rear: 10

Enter your choice: 2
Enter value to add to rear: 20

Enter your choice: 1
Enter value to delete node: 10

Enter your choice: 3
20 -> None