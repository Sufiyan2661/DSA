# +++++++++++++++++++++++++ (26/11/25) Implementation of Stack using Array +++++++++++++++++++++++++++++++++++++++
# Deifinition of stack
class MyStack:
    def __init__(self,capacity):
        
        
        # array to store elements
        self.arr = [0] * capacity
        
        
        # Maximum size of stack
        self.capacity = capacity
        
        # index of  the top element
        self.top = -1
       
    
    
    '''
    push operations() add the element in the stack 
    if the stack is full then it is Overflow
    '''
    def push(self,element):
        if self.top == self.capacity -1:
            print("Stack Overflows")
            return 
        self.top += 1
        self.arr[self.top] = element
        
        
        
    '''
    pop operation() Remove the item from the stack
    the items are popped in the reverse order in 
    which they pushed.
    '''
    def pop(self):
        if self.top == -1:
            print("Stack is Empty")
            return 
        value = self.arr[self.top]
        self.top -= 1
        return value
    
    '''
    top or peek operations on stack
    return the top element of the stack
    '''
    def get_top(self):
        if self.top == -1:
            print("Queue is empty")
            return
        return self.arr[self.top]
    
    
    '''
    isEmpty operations on stack
    '''
    def is_empty(self):
        return self.top == -1
    
    '''
    isFull operations on stack
    '''
    def is_full(self):
        return self.top == self.capacity -1
    
