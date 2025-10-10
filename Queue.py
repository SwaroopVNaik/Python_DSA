# Initialization of Singly Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Initialization of Queue 
class Queue:

    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    # enqueue -> Inserting the Value from Rear
    def enqueue(self, data):
        # In queue's values always insert from Rear
        print(f"Inserting value {data} into the queue")
        new_node = Node(data) 

        # Case_1 : Queue is empty
        if self.rear == None:
            self.front = new_node
        else:
            # Case_2 : Queue has some Node's 
            self.rear.next = new_node
            
        self.rear = new_node
        self.count = self.count + 1

    # dequeue -> Deleting the value From the front
    def dequeue(self) -> int:
        # Case_1: Queue is Empty
        if self.front == None:
            print("The Queue is empty")
            return -100  # returning Error
        
        # Case_2 : Queue is not empty
        return_data = self.front.data
        self.front = self.front.next

        # Special_Case => if there was only one element queue became empty 
        if self.front == None:
            self.rear = None

        self.count = self.count - 1
        print(f"Removing Element {return_data} from the Queue")
        return return_data
    
    # Returns element without removing it
    def peek(self) -> int:
        if self.front == None:
            print("Queue is Empty")
            return -100  # returning error
        return self.front.data
    
    # Count of the elements 
    def get_count(self) -> int:
        return self.count
    
    # Printing all the elements in the List
    def print_all_the_elements(self):
        if self.front == None:
            print("Queue is Empty")
            return 
        
        current_node = self.front
        print("The Elements in the Queue are : ")
        while current_node != None:
            print(f"{current_node.data} --> ", end="")
            current_node = current_node.next
        print()

if __name__ == "__main__":

    my_queue = Queue()

    my_queue.dequeue()
    my_queue.print_all_the_elements()
    print(f"Count: {my_queue.get_count()}")

    my_queue.enqueue(1)
    my_queue.print_all_the_elements()
    print(f"Count: {my_queue.get_count()}")

    my_queue.dequeue()
    Value_1 = my_queue.dequeue()
    print(f"We got value -> {Value_1} from the queue")
    my_queue.print_all_the_elements()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    Value = my_queue.dequeue()
    print(f"We got value -> {Value} from the queue")
    my_queue.print_all_the_elements()
