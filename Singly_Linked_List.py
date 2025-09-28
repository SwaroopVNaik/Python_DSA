# class which represent the node in a Singly_Linked_List..!
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # In Python Null is None..!

# class implements all the operations for Singly_Linked_List..!
class SinglyLinkedlist:
    def _init__(self):
        self.head = None

    # This function add the node at the beginning
    # This needs to handle two scenario/cases
    # 1) when list is empty
    # 2) List has some elements
    def insert_at_beginning(self, data):
        # Create a new node
        new_node = Node(data)

        # Case 1: If the list is empty, make the new_node as head..!
        if (self.head == None):
            self.head = new_node 
            return
        
        # Case 2: If the list is not empty, make the new_node as head and point the head to the old head..!
        new_node.next = self.head
        self.head = new_node
        return

# Driver code to test the above class

if __name__ == "__main__":
    # Create a mew singly Linked List
    list = SinglyLinkedlist()

    list.insert_at_beginning(10)
    list.insert_at_beginning(20)
    list.insert_at_beginning(30)

    print("List is created successfully")
    print("Head Node data is : ", list.head.data)
    print("Next node data is : ", list.head.next.data)
    print("Next node Data is : ", list.head.next.next.data)
