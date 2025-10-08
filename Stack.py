# Class Which represents the Node in Singly_Linked_List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.count = 0 # Number of Elements Present in Stack
        self.top = None # Reference
    
    # Stack Operation -> Push() Inserting the Elements in the stack..!
    def push(self, data):
        new_node = Node(data) # Creating new_node

        # Stack can be either empty or not
        new_node.next = self.top # 1 
        self.top = new_node # 2
        self.count = self.count + 1 # Incrementing
        print(f" the pushed value {data} of the stack ")

    # Stack Operation -> Pop() Removes and returns the top element
    def pop(self) -> int :
        # case_1 : stack is Empty 
        if(self.top == None):
            print(" Stack is Empty, can't perform pop() operations ")
            return -100 # Returning Error
        
        # if the stack is not empty
        data = self.top.data
        self.top = self.top.next
        self.count = self.count - 1 # decrementing
        print(f" the popped element from the stack : {data} ")
        return data
    
    # Stack Operation -> peek() Returns top element without removing it 
    def peek(self) -> int:
        # case_1 : stack is Empty 
        if(self.top == None):
            print(" Stack is Empty, can't perform pop() operations ")
            return -100 # Returning Error
        
        # if stack is not Empty 
        return self.top.data
    
    # Stack Operation -> count() to get count of number of elements present in the stack
    def get_count(self) -> int:
        print(f" there are {self.count} elements in the stack ")
        return self.count 
    
    # Stack Operation -> print() all the node values of the stack
    def print_all_values(self):
        # case_1 : the stack is empty
        if(self.top == None):
            print("The stack is empty ")

        # case_2 = when the stack is not empty
        current_node = self.top
        print(" Elements in the stack are as below ")
        while(current_node is not None):
            print(f"{ current_node.data }")
            current_node = current_node.next

if __name__ == "__main__":

    stack = Stack()

    stack.pop()
    stack.get_count()
    stack.print_all_values()

    stack.push(1)
    stack.get_count()
    stack.print_all_values()
    stack.pop()

    stack.push(1)  
    stack.push(2)
    stack.push(3)  
    stack.push(4)
    stack.push(5)
    stack.print_all_values()
    stack.pop() 
