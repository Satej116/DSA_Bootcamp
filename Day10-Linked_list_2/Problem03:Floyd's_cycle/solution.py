class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_rear(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def create_cycle(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next 
            current.next = prev       
            prev = current            
            current = next_node

        self.head = prev
        print("List reversed successfully.")

    def display(self,position):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Current List:")
        while current:
            print(current.data, end=" -> ")
            if(position == current.data):
                break
            else:
                current = current.next
        else:
            position = 0
        
        return position
            
        
    def has_cycle():
        if (position == 0):
            print(False)
        else:
            print(True)

linked_list = MyLinkedList()

while True:
    print("\nChoose an option:" \
          "\n1. Add to rear" \
          "\n2. Reverse and display list" \
          "\n3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to add to rear: "))
        linked_list.add_to_rear(value)
    elif choice == 2:
        position = int(input("Enter the element to which you have to traverse"))
        linked_list.create_cycle()
        linked_list.display(position)
        linked_list.has_cycle()
    elif choice == 3:
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")
