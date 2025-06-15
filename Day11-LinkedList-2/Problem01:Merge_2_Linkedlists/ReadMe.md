# Merge and Sort Linked Lists in Python

##  Description

This Python program demonstrates the creation, merging, and sorting of **two singly linked lists**. Each list is built dynamically by the user, and the program allows:

- Adding elements to List 1 and List 2
- Displaying both lists
- Merging the two **sorted** lists into one
- Sorting the merged list
- Displaying the final sorted merged list

##  Features

- Linked List implementation using custom `Node` and `LinkedList` classes
- Tail insertion method for list building
- In-place bubble sort for sorting the final list
- Static method to merge two sorted linked lists
- Simple CLI menu to interact with the program

##  How It Works

1. **Add to List 1 / List 2**  
   Adds integers to the end of the specified linked list.

2. **Display List**  
   Prints the elements in the selected list in order.

3. **Merge Both Sorted Lists**  
   Merges List 1 and List 2 assuming both are already sorted.  
   (You can manually enter them in sorted order or use the `.sort()` method before merging.)

4. **Display Sorted Merged List**  
   Sorts and displays the merged list.

## Example

Enter value to add to List 1: 2
Enter value to add to List 1: 6
Enter value to add to List 2: 1
Enter value to add to List 2: 7
Merged successfully!
Sorted Merged List:
1 -> 2 -> 6 -> 7 -> None