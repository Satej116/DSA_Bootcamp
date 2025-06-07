def initial():
    stack1 = []
    stack2 = []
    return stack1, stack2

def enqueue_f(stack1, stack2):
    a = int(input("Enter the Number to Append: "))
    stack1.append(a)
    stack2.append(a)

def dequeue_f(stack1, stack2):
    if not stack2:
        print("Queue is empty")
        return
    b = stack2.pop(0) 
    print("Removed Element =", b)
    stack1.remove(b)

def peek_f(stack1):
    if not stack1:
        print("Queue is empty")
    else:
        print("Front Element =", stack1[0])

def is_empty_f(stack1, stack2):
    if not stack1 and not stack2:
        print("Queue is empty")
    else:
        print("Queue is not empty")

def implementation(stack1, stack2):
    while True:
        print("\nChoose an Option:\n"
        "1. Enqueue\n" 
        "2. Dequeue\n" 
        "3. Peek\n" 
        "4. Is Empty\n" 
        "5. Exit")

        x = int(input("Enter option number: "))

        if x == 1:
            enqueue_f(stack1, stack2)
        elif x == 2:
            dequeue_f(stack1, stack2)
        elif x == 3:
            peek_f(stack1)
        elif x == 4:
            is_empty_f(stack1, stack2)
        elif x == 5:
            break
        else:
            print("Choose a valid option")

stack1, stack2 = initial()
implementation(stack1, stack2)
