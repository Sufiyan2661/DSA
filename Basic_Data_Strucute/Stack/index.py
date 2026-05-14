# Basic Problems of stack 
# Stack using Array
class Stack:
    def __init__(self,capacity:int):
        self.arr = [0] * capacity
        
        self.capacity = capacity
        
        self.top = -1
        
    def is_full(self):
        return self.top == self.capacity - 1
    
    
    def push(self,data:any):
        if self.is_full():
            print("Stack overflows.")
            return
        self.top += 1
        self.arr[self.top] = data
    
    def pop(self):
        if self.top < 0:
            print("Stack is empty")
            return
        elem = self.arr[self.top]
        del self.arr[self.top]
        self.top -= 1
        return elem
    
    def peak(self):
        if self.top < 0:
            print("Stack is empty.")
            return
        return self.arr[self.top] 
    
    def middle(self):
        if self.top < 0:
            print("Stack is empty ")
            return
        
        mid = self.capacity // 2
        mid_elem = self.arr[mid]
        del self.arr[mid]
        self.top -= 1
        return mid_elem
    



    
def sort_stack(stack):

    if len(stack) != 0:

        temp = stack.pop()

        sort_stack(stack)

        insert_sorted(stack, temp)


def insert_sorted(stack, element):

    if len(stack) == 0 or stack[-1] <= element:
        stack.append(element)
        return

    temp = stack.pop()

    insert_sorted(stack, element)

    stack.append(temp)
        
                
        
        
        


if __name__ == "__main__":
    st = Stack(5)
    st.push(8)
    st.push(3)
    st.push(5)
    st.push(5)
    st.push(6)
    sort_stack(st.arr)
    print("Middle ",st.middle())
    print("Peak ",st.peak())
    
    
    
    
# Stack Using Linked List

# class Node:
#     def __init__(self,data):
        
        
#         self.data = data
#         self.next = None
        


# class Stack:
#     def __init__(self):
        
#         self.top = None
        
        
#     def is_empty(self):
#         return self.top is None
    
#     def push(self,data):
#         temp = Node(data)
#         temp.next = self.top
#         self.top = temp
    
#     def peak(self):
        
#         if not self.top:
#             print("There are no elements ")
#             return 
#         return self.top.data
    
#     def pop(self):
#         if not self.top:
#             print("Stack is empty")
#             return
#         temp = self.top 
#         self.top = self.top.next
#         val  = temp.data
#         del temp
#         return val
    
        
    
        


# if __name__ == "__main__":
#     st = Stack()
#     print("stack is emtpy ",st.is_empty())
#     st.push(1)
#     st.push(2)
#     st.push(4)
#     st.push(5)
#     st.pop()
    
#     print("Last Element ",st.peak())
#     print("stack empty ",st.is_empty())
    



'''
Check Balanced Parentheses
"({[]})" -> True
"([)]" -> False

'''
# Using Array for stack
# def balanced_paranthesis(s:str) -> bool:
#     st = Stack(len(s))
#     mapping = {
#         ")":"(",
#         "}":"{",
#         "]":"["
#     }
    
    
    
#     for ch in s:
        
#         # for closing bracket
#         if ch in mapping:
            
#             if st.top < 0:
#                 return False
            
            
#             top = st.peak()
            
#             if mapping[ch] == top:
#                 st.pop()
#             else:
#                 return False
#         else:
#             st.push(ch)
        
#     return st.top < 0



# if __name__ == "__main__":
#     s = "({[]})"
#     print("Balanced ",balanced_paranthesis(s=s))
    
    
# def balanced_paranthesis(s:str) -> bool:
#     st = Stack()
#     mapping = {
#         ")":"(",
#         "}":"{",
#         "]":"["
#     }
#     for ch in s:
        
#         # for closing brackets:
#         if ch in mapping:
            
#             if st.top == None:
#                 return False
            
#             top = st.peak()
            
#             if mapping[ch] == top:
#                 st.pop()
#             else:
#                 return False
            
#         else:
#             st.push(ch) 
#     return st.top is None

# if __name__ == "__main__":
#     s = "({[]})"
#     print("Balanced ",balanced_paranthesis(s=s))
    


# def reverse_string(s:str) -> str:
#     st = Stack(len(s))
#     new_string = ""
#     for ch in s:
#         st.push(ch)
#     for ch in s:
#         new_string += st.pop()
    
#     print("reverse string ",new_string)
        


# if __name__ == "__main__":
    
#     reverse_string("abc")








