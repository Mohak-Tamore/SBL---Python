class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    # function to add an element to the linked list
    def add_element(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
    # function to remove an element from the linked list
    def remove_element(self, data):
        if self.head is None:
            print("List is empty!")
            return
        elif self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next
            print("Element not found in the list!")
    
    # function to replace an element in the linked list
    def replace_element(self, old_data, new_data):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        print("Element not found in the list!")
        
    # function to search for an element in the linked list
    def search_element(self, data):
        if self.head is None:
            print("List is empty!")
            return
        current = self.head
        while current is not None:
            if current.data == data:
                print("Element found in the list!")
                return
            current = current.next
        print("Element not found in the list!")
        
    # function to display the linked list
    def display_list(self):
        if self.head is None:
            print("List is empty!")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next


# main program
my_list = LinkedList()

while True:
    print("\nMenu:")
    print("1. Add an element\n2. Remove an element\n3. Replace an element\n4. Search for an element\n5. Display the linked list\n6. Quit\n")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            data = input("Enter Student's name: ")
            my_list.add_element(data)
        case 2:
            data = input("Enter the name of the student to be removed: ")
            my_list.remove_element(data)
        case 3:
            old_data = input("Enter the name of the student to be replaced: ")
            new_data = input("Enter the name of new student: ")
            my_list.replace_element(old_data, new_data)
        case 4:
            data = input("Enter the name to search for: ")
            my_list.search_element(data)
        case 5:
            my_list.display_list()
        case 6:
            break
        case other:
            print("Incorrect option!")