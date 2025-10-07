# This class represents data
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Circular_List:
    def __init__(self):
        self.tail = None

    # This Function insert a node after tail(start)
    # if there is a node at start then it becomes a second node 
    # Here, tail node Remains the Same
    # Time Complexity O(1)
    def insert_at_beginning(slef, data):
        # Create new node 
        new_node = Node(data)
        # Case_1 : Empty List
        if(slef.tail == None):
            slef.tail = new_node
            new_node.next = new_node
            return

        # Case_2 : Single Node / Multi - Node (Both Cases)
        new_node.next = slef.tail.next
        slef.tail.next = new_node

    # This Function insert node at tail and new node becomes the tail
    # If there is new_node at then end then it becomes the tail
    # here, head node remains the Same
    # Time Complexity O(1)
    def insert_at_tail(self, data):
        new_node = Node(data)

        # Case_1 : Empty List
        if(self.tail == None):
            self.tail = new_node
            new_node.next = new_node
            return
        
        # we don't know the address of node before the tail node.
        # Case_2 : Single Node / Multi - Node 
        new_node.next = self.tail.next # 1
        self.tail.next = new_node # 2
        self.tail = new_node # changing reference (3)
        return
    
    # Delete the node after tail node 
    # tail remains the same
    def delete_at_beginning(slef):

        # Case_1 : List is Empty
        if(slef.tail == None):
            print(" List is Empty ")
            return
        
        # Case_2 : Single_Node (list will become empty)
        if(slef.tail.next == slef.tail):
            slef.tail = None
            return
        
        # Case_3 : Multi - Node ( two or more )
        slef.tail.next  = slef.tail.next.next 
    
    # node before tail becomes the new tail
    # since we don't have address of node before tail node we have to traverse to reach there
    def delete_at_tail(self):
        # Case_1 : Empty list
        if(self.tail == None):
            return
        
        # Case_2 : Single Node 
        if(self.head.next == self.head):
            self.tail = None
            return
        
        # Case_3 : Multi - Node (two or more )
        new_tail = self.tail.next # (copying reference)
        while(new_tail.next != self.tail):
            new_tail = new_tail.next

        new_tail.next = self.tail.next
        self.tail = new_tail
    
    def print_all_nodes(self):
        # Case_1 : List is Empty
        if(self.tail == None):
            print("List is Empty")
            return

        current_node = self.tail.next
        while(True):
            print(f"{current_node.data} --> ")

            if(current_node == self.tail):
                break
            
            current_node = current_node.next
        # This is After While Loop 

    def search_key(self, key):
        # Case_1 : List is Empty
        if(self.tail == None):
            print("List is Empty")
            return

        current_node = self.tail.next
        while(True):
            if(current_node.data == key):
                print(" key is found in the list ")
                return

            # To demonstarte "demo_infinite_loop" comment this if condition 👇 (DEBUG)
            if(current_node == self.tail):
                break
            
            current_node = current_node.next 
        print(" Key is not found in the List ")

def Circular_Linked_List_Tests(clist : Circular_List):

    # List is empty trying to delete a node
    clist.delete_at_beginning()
    clist.delete_at_tail()
    clist.print_all_nodes()
    clist.search_key(40)

    # perform insert and delete single node
    clist.insert_at_beginning(10)
    clist.delete_at_beginning()

    clist.insert_at_tail(30)
    clist.delete_at_tail()

    # Create List with multiple nodes
    clist.insert_at_beginning(10)
    clist.print_all_nodes()
    clist.search_key(40)



    clist.insert_at_beginning(20)
    clist.insert_at_beginning(30)
    
    clist.insert_at_tail(40)
    clist.print_all_nodes()
    clist.search_key(40)
    clist.search_key(700)

def demo_infinite_loop(clisit: Circular_List):
    clist.insert_at_beginning(10)
    clist.insert_at_beginning(20)
    clist.insert_at_beginning(30)
    clist.insert_at_beginning(40)

    clist.search_key(700)


if __name__== "__main__":
    clist = Circular_List()
    Circular_Linked_List_Tests(clist)

    demo_infinite_loop(clist)