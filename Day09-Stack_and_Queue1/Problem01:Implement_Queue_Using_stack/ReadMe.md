# Queue Implementation using Two Stacks

This Python script implements a basic **Queue** data structure using two **Stacks** (`stack1` and `stack2`). It provides the fundamental queue operations: enqueue, dequeue, peek, and check if empty.

## Features

- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove and return the front element.
- **Peek**: View the front element without removing it.
- **Is Empty**: Check whether the queue is empty.
- **Interactive Menu**: User selects operations in a loop until they choose to exit.

## How It Works

- Two stacks (`stack1` and `stack2`) are used:
  - `stack1` stores the original order.
  - `stack2` enables queue-like behavior via element shifting.
- `dequeue` and `peek` operations work from `stack2`.

## Sample Menu

Choose an Option:

Enqueue

Dequeue

Peek

Is Empty

Exit

shell
Copy
Edit

## Example Run

Enter option number: 1
Enter the Number to Append: 10

Enter option number: 1
Enter the Number to Append: 20

Enter option number: 2
Removed Element = 10

Enter option number: 3
Front Element = 20

markdown
Copy
Edit

## Code Design

- The program uses a loop-based interface.
- Functions are modular:
  - `enqueue_f`: Adds an element.
  - `dequeue_f`: Removes the front element.
  - `peek_f`: Shows the front.
  - `is_empty_f`: Checks queue emptiness.
- The `implementation()` function handles user interaction.
