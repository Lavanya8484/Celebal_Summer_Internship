class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):  #add to end Function 
        new_node = Node(value)
      
        #if list is empty
        if self.head is None:
            self.head = new_node
            print(f"Added {value} as the first node.")
            return

        #if list is not empty
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added {value} at the end.")

    def show(self):
        #printing values in the list 
        if self.head is None:
            print("The list is empty.")
            return

        current = self.head
        print("Linked List: ", end="")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def delete_at_position(self, position):
        #deleting at a specified posistion 
        if self.head is None:
            raise IndexError("You can't delete from an empty list.")

        if position <= 0:
            raise IndexError("Position must be 1 or more.")

        if position == 1:
            print(f"Deleted node at position {position} with value {self.head.value}")
            self.head = self.head.next
            return

        current = self.head
        count = 1

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            raise IndexError("Position out of range.")

        print(f"Deleted node at position {position} with value {current.next.value}")
        current.next = current.next.next


if __name__ == "__main__":
    my_list = LinkedList()

    # adding values 
    my_list.add_to_end(5)
    my_list.add_to_end(15)
    my_list.add_to_end(25)
    my_list.add_to_end(35)
    my_list.show()

    #deleting some node values 
    try:
        my_list.delete_at_position(2)
        my_list.show()

        my_list.delete_at_position(1)
        my_list.show()

        my_list.delete_at_position(10) #as the 10th index doesnot exist it'll cause an error  
        
    except IndexError as error:
        print("Oop's can't delete:", error)

    #Trying to delete an empty List
    empty_list = LinkedList()
    try:
        empty_list.delete_at_position(1)
    except IndexError as error:
        print("The list is empty:", error)



'''Output:

Added 5 as the first node.
Added 15 at the end.
Added 25 at the end.
Added 35 at the end.
Linked List: 5 -> 15 -> 25 -> 35 -> None
Deleted node at position 2 with value 15
Linked List: 5 -> 25 -> 35 -> None
Deleted node at position 1 with value 5
Linked List: 25 -> 35 -> None
Oop's can't delete: Position out of range.
The list is empty: You can't delete from an empty list.

'''

