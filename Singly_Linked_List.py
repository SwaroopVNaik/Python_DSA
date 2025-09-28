# class which represent the node in a Singly_Linked_List..!
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # In Python Null is None..!

# class implements all the operations for Singly_Linked_List..!
class SinglyLinkedlist:
    def __init__(self):
        self.head = None

    # This function add the node at the beginning.
    # This needs to handle two scenario/cases.
    # 1) when list is empty.
    # 2) List has some elements.
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
    
    # This Function Adds the node at the end of the Linked list.
    # it needs to handle the two cases/scenario. 
    # 1) when list is empty.
    # 2) when list has only one node.
    # 3) when List has more then one node.

    def Insert_at_end(self, data):
        # create a object of type Node
        new_node = Node(data)

        # 1) when List is empty
        if(self.head == None):
            self.head = new_node
            return
        
        # 2) When List has only one Node
        if(self.head.next == None):
            self.head.next = new_node
            return
        
        # 3) When List has more then one Node loop till the last Node
        # Time Complexity -> O(n)
        current_node = self.head # declaring the temp Variable to store the (self.head) address
        while(current_node.next != None):
            current_node = current_node.next

        # set the last node next to the new_node
        current_node.next = new_node
        return

# This code is outside the class SinglyLinkedList
# Driver Code to test the above class

# Insert at the beginning..!
def insert_at_the_beginning_driver(list : SinglyLinkedlist):
    list.insert_at_beginning(10)
    list.insert_at_beginning(20)
    list.insert_at_beginning(30)

    print("List is created successfully")
    print("Head Node data is : ", list.head.data)
    print("Next node data is : ", list.head.next.data)
    print("Next node Data is : ", list.head.next.next.data)

# Insert at the end..!
def insert_at_the_end_driver(list : SinglyLinkedlist):
    list.Insert_at_end(10)
    list.Insert_at_end(20)
    list.Insert_at_end(30)
    list.Insert_at_end(40)


if __name__ == "__main__":
    # Create a mew singly Linked List
    list = SinglyLinkedlist()

    insert_at_the_beginning_driver(list)

    insert_at_the_end_driver(list)