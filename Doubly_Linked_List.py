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
if __name__ == "__main__":
    
    dlist = Doubly_Linked_list() # calling constructor

    insert_at_beginning_test(dlist)

    insert_at_end_test(dlist)

