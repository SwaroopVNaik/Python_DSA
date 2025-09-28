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
    
    def print_list(self):
        # when list is empty
        if(self.head == None):
            print("List is empty")
            return
        
        current_node = self.head
        while(current_node != None ):
            print(str(current_node.data) + " --> ")
            current_node = current_node.next

    def search(self, key):
        # when list is empty
        if(self.head == None):
            print("List is empty")
            return
        
        current_node = self.head

        while(current_node != None ):
            print(str(current_node.data) + " --> ")

            if(key == current_node.data):
                print(" Given key is present in the List")
                return
            
            current_node = current_node.next

        print("Given Key is not present in the List")

    def delete_at_beginning(self):
        # 1) List is Empty 
        if (self.head == None):
            return
        
        # 2) List has only one node
        if (self.head.next == None):
            self.head = None
            return
        
        # 3) list has two or more nodes present
        self.head = self.head.next

    def delete_at_end(self):
        # 1) list is empty 
        if (self.head == None):
            return
        
        # 2) list has only one node 
        if (self.head.next == None):
            self.head = None
            return
        
        # 3) list has two or more nodes present
        current_node = self.head
        while (current_node.next.next != None):
            current_node = current_node.next
        
        current_node.next = None


    def insert_at_position(self, data, insert_position):
    
        # Position is Invalid
        if(insert_position <= 0):
            print("Invalid Position")
            return

        # Insert at the first Postion
        if(insert_position == 1):
            self.insert_at_beginning(data)
            return

        # insert at position 2 or greater 
        current_node = self.head
        current_position = 1

        while(current_position < insert_position - 1 and current_node is not None):
            current_position = current_position + 1
            current_node = current_node.next

        if(current_node == None):
            print("Invalid Position, there are lesser number of nodes")
            return
        
        new_node = Node(data)
        new_node.next = current_node.next 
        current_node.next = new_node


    def delete_at_position(self, delete_position):
    
        # Position is Invalid
        if(delete_position <= 0):
            print("Invalid Position")
            return

        # Delete at the first Postion
        if(delete_position == 1):
            if self.head is not None:
                self.head = self.head.next
            return

        # delete at position 2 or greater 
        current_node = self.head
        current_position = 1

        while(current_position < delete_position - 1 and current_node is not None):
            current_position = current_position + 1
            current_node = current_node.next

        if(current_node == None or current_node.next == None):
            print("Invalid Position, there are lesser number of nodes")
            return
            
        current_node.next = current_node.next.next 


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

# Insert / delete at given Position..!
def insert_delete_at_given_position_driver(list : SinglyLinkedlist):
    list.insert_at_position(10, -1)
    list.delete_at_position(-1)

    list.insert_at_position(10, 1)
    list.delete_at_position(1)

    list.Insert_at_end(10)
    list.Insert_at_end(20)
    list.Insert_at_end(30)

    list.insert_at_position(15, 2)
    list.insert_at_position(40, 4)
    list.insert_at_position(100, 10)

# print search nodes...!
def print_search_list_driver(list: SinglyLinkedlist):
    list.print_list()

    list.Insert_at_end(10)
    list.print_list()

    list.Insert_at_end(20)
    list.Insert_at_end(30)
    list.print_list()

    list.search(100)
    list.search(20)

# Delete at beginning
def delete_operations_start_end(list : SinglyLinkedlist):
    list.delete_at_beginning()
    list.delete_at_end()

    list.insert_at_beginning(10)
    list.delete_at_beginning()

    list.insert_at_beginning(10)
    list.delete_at_end

    list.insert_at_beginning(10)
    list.insert_at_beginning(20)
    list.insert_at_beginning(30)
    list.delete_at_end()
    list.delete_at_end()


if __name__ == "__main__":
    # Create a new singly Linked List
    list = SinglyLinkedlist()

    insert_at_the_beginning_driver(list)

    insert_at_the_end_driver(list)

    insert_delete_at_given_position_driver(list)

    print_search_list_driver(list)

    delete_operations_start_end(list)

