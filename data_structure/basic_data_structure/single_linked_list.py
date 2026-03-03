class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def delete_first(self):
        if self.head == None:
            print("linked list is empty")
            return
        value = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None

    def delete_end(self):
        if self.head == None:
            print("list is empty")
            return
        if self.head.next == None:
            value = self.head.data
            self.head = None
            self.tail = None
            return

        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        Value = self.tail.data
        temp.next = None
        self.tail = temp

    def search(self, key):
        temp = self.head
        while temp != None:
            if key == temp.data:
                return True
            temp = temp.next
        return False

    def display(self):
        if self.head == None:
            print("list is empty")
            return
        temp = self.head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next


def run_linked_list():
    ll = LinkedList()

    while True:
        print("\n--- Linked List Operations ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Delete first")
        print("4. Delete last")
        print("5. Search")
        print("6. Display")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            value = int(input("Enter value: "))
            ll.insert_first(value)

        elif choice == 2:
            value = int(input("Enter value: "))
            ll.insert_last(value)

        elif choice == 3:
            ll.delete_first()

        elif choice == 4:
            ll.delete_end()

        elif choice == 5:
            value = int(input("Enter value to search: "))
            if ll.search(value) == True:
                print(f"{value} is found in list")
            else:
                print("not found")

        elif choice == 6:
            ll.display()

        elif choice == 7:
            print("Exiting.")
            break

        else:
            print("Invalid option. Try again.")


# Run the loop
run_linked_list()
