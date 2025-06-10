class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def delete_node(self, data):
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

        print(f"Value {data} not found in the list.")

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
          "\n1. Delete node" \
          "\n2. Add value at tail" \
          "\n3. Display list" \
          "\n4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to delete node: "))
        linked_list.delete_node(value)
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
