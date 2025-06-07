class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_to_rear(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = MyLinkedList()

while True:
    print("\nChoose an option:" \
          "\n1. Add to front" \
          "\n2. Add to rear" \
          "\n3. Display list" \
          "\n4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to add to front: "))
        linked_list.add_to_front(value)
    elif choice == 2:
        value = int(input("Enter value to add to rear: "))
        linked_list.add_to_rear(value)
    elif choice == 3:
        linked_list.print_list()
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")
