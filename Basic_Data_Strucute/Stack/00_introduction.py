# +++++++++++++++++++++++++ (26/11/25) Implementation of Stack using Array +++++++++++++++++++++++++++++++++++++++
# Deifinition of stack
# class MyStack:
#     def __init__(self,capacity):
        
        
#         # array to store elements
#         self.arr = [0] * capacity
        
        
#         # Maximum size of stack
#         self.capacity = capacity
        
#         # index of  the top element
#         self.top = -1
       
    
    
#     '''
#     push operations() add the element in the stack 
#     if the stack is full then it is Overflow
#     '''
#     def push(self,element):
#         if self.top == self.capacity -1:
#             print("Stack Overflows")
#             return 
#         self.top += 1
#         self.arr[self.top] = element
        
        
        
#     '''
#     pop operation() Remove the item from the stack
#     the items are popped in the reverse order in 
#     which they pushed.
#     '''
#     def pop(self):
#         if self.top == -1:
#             print("Stack is Empty")
#             return 
#         value = self.arr[self.top]
#         self.top -= 1
#         return value
    
#     '''
#     top or peek operations on stack
#     return the top element of the stack
#     '''
#     def get_top(self):
#         if self.top == -1:
#             print("Queue is empty")
#             return
#         return self.arr[self.top]
    
    
#     '''
#     isEmpty operations on stack
#     '''
#     def is_empty(self):
#         return self.top == -1
    
#     '''
#     isFull operations on stack
#     '''
#     def is_full(self):
#         return self.top == self.capacity -1

#     '''
#     Traverse() 
#     '''
#     def traverse(self):
#         if self.is_empty():
#             print("Stack is empty")
#             return
#         for i in range(self.top,-1,-1):
#             print(self.arr[i])



# if __name__ == "__main__":
#     q = MyStack(3)
#     q.push(10)
#     q.push(20)
#     q.push(30)
    
#     # print("The popped element ",q.pop())
#     print("The stack is full",q.is_full())
#     q.traverse()

# +++++++++++++++++++++++++++++++++++++ (27/11/25) Stack Using Linked List ++++++++++++++++++++++++++++++++
# Decleration of stack using linked list
# First declare the node
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# # Then declare the stack
# class MyStack:
#     def __init__(self):
#         # Initially stack is empty
#         self.top = None
    
    
#     '''
#     Push Operation:- Adds an item to the stack. Unlike array there is no fixed 
#     capacity in linked list. Overflow occurs only when memory is exhausted
#     '''
    
#     def push(self,value):
#         # create new node
#         new_node = Node(value)
        
#         # Point the new node`s next pointer to top node
#         new_node.next = self.top
        
#         # update the top pointer to point to this new node
#         self.top = new_node
    
    
#     '''
#     Pop Operation:-Removes top item from the stack. If the stack is empty 
#     then it is said to Underflow condition. 
#     '''
    
#     def pop(self):
#         if self.top == None:
#             print("Stack is empty")
#             return
#         # Store current top in temp variable
#         temp = self.top
        
#         # Move top pointer to next node
#         self.top = self.top.next
        
#         val = temp
        
#         del temp
#         return val
    
    
#     '''
#     peek or top operation:- Return the value of the top item without 
#     removing it from the stack.
#     '''
#     def get_top(self):
#         if self.top == None:
#             print("Stack is empty")
#             return -1
#         return self.top.data
    
    
#     '''
#     isEmpty Operation:- Checks whether the stack has elemtns.
#     '''
#     def is_empty(self):
#         return self.top is None

    
#     '''
#     Traverse Operation
#     '''
    
#     def traverse(self):
#         if self.is_empty():
#             print("Stack is empty")
#             return
#         while self.top:
#             print(self.top.data)
#             self.top = self.top.next
        
        

# if __name__ == "__main__":
#     s = MyStack()
#     s.push(10)
#     s.push(20)
#     s.push(30)
    
#     s.pop()
    
#     s.traverse()


    