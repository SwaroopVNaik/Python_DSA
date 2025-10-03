# Class which represents Doubly_Linked_List 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
#-------------------------------------------------------------------------------------------------

# Class Represents all the Operations of Doubly_Linked_list
class Doubly_Linked_list:
    def __init__(self):
        self.head = None
#--------------------------------------------------------------------------------------------------
# Inserting Node In the Beginning Case_1, Case_2
    def insert_at_beginning(self, data):

        # Creating the Node
        new_node = Node(data) # Invoking The constructor of Node

        # Case_1: List is Empty 
        if(self.head == None):
            self.head = new_node
            return
        
        # No need of changing the ( prev_node ) or ( next_node ) as it will be pointing to the None 
        # only we have to point ( head -> None ) to ( head -> new_node )
#--------------------------------------------------------------------------------------------------
        # Case_2: List has One or more Node's
        new_node.next = self.head # 1 
        self.head.prev = new_node # 2
        self.head = new_node # 3
        return
#--------------------------------------------------------------------------------------------------
# Inserting Node in the End Case_1, Case_2
    def insert_at_the_end(self, data):

        # Creating New Node 
        new_node = Node(data) # Invoking the Constructor of Node

        # Case_1: List is empty
        if(self.head == None):
            self.head = new_node
            return
        
        # No need of changing the ( prev_node ) or ( next_node ) as it will be pointing to the None 
        # only we have to point ( head -> None ) to ( head -> new_node )
#--------------------------------------------------------------------------------------------------
        # Case_2 : List has only one Node
        if(self.head.next == None):
            self.head.next = new_node
            new_node.prev = self.head
            return
#--------------------------------------------------------------------------------------------------
        # Case_3: List has more then one Node
        last_node = self.head
        # Loop until the Current_node is None..!
        while(last_node.next != None):
            last_node = last_node.next 
        
        # Implementing Logic
        last_node.next = new_node
        new_node.prev = last_node
        return
#-------------------------------------------------------------------------------------------------
    # Inserting Node at the postion's Case_1, Case_2, Case_3, Case_4, 
    def insert_at_position(self, data, target_position):

        # Creating a New Node ->
        new_node = Node(data) # Invoking the constructor of Node

        # Case_1: List position <= 0
        if(target_position <= 0):
            print("Invalid position")
            return
#--------------------------------------------------------------------------------------------------
        # Case_2 : When List is empty, we can only support insert at position 1
        if(self.head == None and target_position != 1):
            print("Invalid Postion")
            return
#-------------------------------------------------------------------------------------------------
        # Case_3 : List has only one Node 
        if(self.head.next == None and target_position > 2 ):
            print("Invalid Position")
            return
#------------------------------------------------------------------------------------------------   
        # Case_4 : Inserting at beginnning
        if(target_position == 1):
            self.insert_at_beginning(data)
            return
#------------------------------------------------------------------------------------------------
        # Logic for finding the last_node
        current_postion = 1
        current_node = self.head
        while(current_node != None and current_postion < target_position - 1):
            current_postion = current_postion + 1
            current_node = current_node.next
        
        if(current_node == None):
            print("Invalid Position")
            return
        
        # When we Inserting between two Node's, We need these steps # 1 and # 2..!
        if(current_node.next != None):
            current_node.next.prev = new_node # 1
            new_node.next = current_node.next # 2

        # These are need for Inserting in between and also at the End..!
        current_node.next = new_node # 3
        new_node.prev = current_node # 4 

#--------------------------------------------------------------------------------------------------
    #Printing all the Nodes Case_1, Case_2, Case_3
    def print_all_NODEs(self):
        print("\nPrinting all the nodes in Doubly_Linked_List")
        # Case_1 : List is Empty
        if(self.head == None):
            print("\nList is Empty")
            return
#---------------------------------------------------------------------------------------------------
        """ <- (Multi Line Comment in Python)
        # Case_2 : List has only one Node
        if(self.head.next == None):
            print(f"<-- {self.head.data} -->", end = " ")
            return
        """ # <- (Multi Line Comment In Python)
#--------------------------------------------------------------------------------------------------
        # Case_3 : List has more then One Node 
        current_Node = self.head
        while(current_Node != None):
            print(f"<-- {current_Node.data} --> ", end = " " )

            # To move the current_Node Pointer Forward
            current_Node = current_Node.next
#-------------------------------------------------------------------------------------------------
    # Searching The Nodes in The Doubly_Linked_list Case_1, Case_2 
    def search(self, key):
        # Case_1 : List is Empty 
        if(self.head == None):
            print("\n Element Key Is Not Found In The List..!")
            return
#--------------------------------------------------------------------------------------------------          
        # Case_2 : List Has One Or More Node's 
        current_Node = self.head
        while(current_Node != None):
            if(current_Node.data == key):
                print("Key is Found in the List..!")
                return
                
            # To move the current_Node Pointer Forward
            current_Node = current_Node.next

        # If we Reach Here it means Key is not Found The List 
        print("KEY IS NOT FOUND IN THE LIST ..!")
#--------------------------------------------------------------------------------------------------
    # Deleting the Nodes at the Beginning of Doubly_Linked_list Case_1, Case_2, Case_3    
    def delete_at_beginning(slef):
        # Case_1 : List is Empty 
        if(slef.head == None):
            return
#--------------------------------------------------------------------------------------------------        
        # Case_2 : List has only One node 
        if(slef.head.next == None):
            slef.head = None
            return
#-------------------------------------------------------------------------------------------------        
        # Case_3 : List has two or more Nodes
        slef.head = slef.head.next
        slef.head.prev = None
        return
#-------------------------------------------------------------------------------------------------
    # Deleting the Nodes at the End of Doubly_Linked_list Case_1, Case_2, Case_3    
    def delete_at_end(slef):
        # Case_1 : List is Empty
        if(slef.head == None):
            return
#-------------------------------------------------------------------------------------------------        
        # Case_2 : List has only one Node 
        if(slef.head.next == None):
            slef.head = None
            return
#------------------------------------------------------------------------------------------------
        # Case_3 : List has two or more Nodes
        # Loop till we get Current_node to current but one node
        current_node = slef.head
        while(current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None
#-------------------------------------------------------------------------------------------------
    def delete_at_position(slef, target_position):
        # Case_1 : List is Empty
        if(slef.head == None):
            print("List is Empty")
            return

        # Case_2 : Position is InValid
        if (target_position <= 0):
            print(f"Invalid position {target_position}")
            return

        # Case_3 : List Has one Node 
        if(slef.head.next == None):
            slef.head = None
            return

        # Case_4 : List has Two or more Nodes
        To_Be_Deleted = slef.head
        current_position = 1

        while(current_position < target_position and To_Be_Deleted is not None):
            current_position = current_position + 1
            To_Be_Deleted = To_Be_Deleted.next

        if (To_Be_Deleted == None):
            print(f"Target Position {target_position} is Invalid , we have lesser Number")
            return
        
        # Case_4.1 : There are nodes after the to_be_deleted node 
        if(To_Be_Deleted == None):
            To_Be_Deleted.prev.next = None
            return
        
        # Case_4.2 : to _be_deleted node is the last node
        To_Be_Deleted.next.prev = To_Be_Deleted.prev
        To_Be_Deleted.prev.next = To_Be_Deleted.next
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
# Test_code :->

# Insert at beginning
def insert_at_beginning_test(dlist: Doubly_Linked_list):
    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
#--------------------------------------------------------------------------------------------------
# Insert at End
def insert_at_end_test(dlist : Doubly_Linked_list):
    dlist.insert_at_the_end(10)
    dlist.insert_at_the_end(20)
    dlist.insert_at_the_end(30)
    dlist.insert_at_the_end(40)
#--------------------------------------------------------------------------------------------------
# insert at position
def insert_at_position_test(dlist : Doubly_Linked_list):
    dlist.insert_at_position(10, -1)
    dlist.insert_at_position(10, 2)
    dlist.insert_at_position(10, 1)
    dlist.insert_at_position(20, 1)
    dlist.insert_at_position(30, 2)
    dlist.insert_at_position(30, 10)
    dlist.insert_at_position(40, 3)
    dlist.insert_at_position(50, 3)
#---------------------------------------------------------------------------------------------------
# print all NODEs
def print_all_NODEs_test(dlist : Doubly_Linked_list):
    dlist.print_all_NODEs()
    dlist.insert_at_beginning(10)
    dlist.print_all_NODEs()

    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.print_all_NODEs()
#-------------------------------------------------------------------------------------------------
# Searching Key in The List 
def search_test(dlist : Doubly_Linked_list):
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)

    dlist.search(100)
    dlist.search(30)
#--------------------------------------------------------------------------------------------------
# Deleting Node at the beginning and End
def delete_tests(dlist : Doubly_Linked_list):
    dlist.delete_at_beginning()
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.delete_at_beginning

    dlist.insert_at_beginning(10)
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.delete_at_end()
#--------------------------------------------------------------------------------------------------
# Delete Node at specified Position 
def delete_at_position_test(dlist : Doubly_Linked_list):
    dlist.delete_at_position(-1)
    dlist.delete_at_position(1)

    dlist.insert_at_beginning(10)
    dlist.delete_at_position(-1)
    dlist.delete_at_position(1)

    dlist.insert_at_beginning(40)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(10)

    dlist.delete_at_position(4)
    dlist.delete_at_position(2)

#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    dlist = Doubly_Linked_list() # calling constructor

    insert_at_beginning_test(dlist)

    insert_at_end_test(dlist)

    insert_at_position_test(dlist) 

    print_all_NODEs_test(dlist)

    search_test(dlist) 

    delete_tests(dlist)

    delete_at_position_test(dlist)