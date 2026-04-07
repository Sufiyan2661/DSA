'''
Q1 : Middle Node in a Linked List

'''

# Naive Approach Two traversal 
# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def count_length_of_node(head:Node)->int:
#     length = 1
    
#     while head.next:
#         length += 1
#         head = head.next
        
#     return length


# def middle_of_linked_list(head:Node) -> int:
#     length = count_length_of_node(head)
    
#     print("Total length of Linked list ",length)
    
    
#     middle = length // 2
#     while middle:
#         head = head.next
#         middle -= 1
        
        
#     return head.data


'''
tc  = O(n*2)
sc = O(1    )
'''

# if __name__ == "__main__":
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
    
    
#     print("Element at middle ",middle_of_linked_list(head=head))    




# [Expected Approach] Hare and Tortoise Algorithm - O(n) Time and O(1) Space


# We can use the Tortoise and Hare algorithm to find the middle of the linked list.

# Initialize both slow and fast pointers at the head.
# Move slow by one step and fast by two steps each iteration.
# When fast reaches the end (or null), slow will be at the middle.
# For even nodes, slow automatically ends at the second middle.



class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
# def get_linked_list_middel(head:list)->int:
    
#     fastptr = head
#     slowptr = head
    
    
#     while fastptr is not None and fastptr.next is not None:
#         fastptr = fastptr.next.next
#         slowptr = slowptr.next
    
    
#     return slowptr.data


'''
tc = O(n)
sc = O(1)

'''

# if __name__ == "__main__":
    
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
#     head.next.next.next.next.next = Node(60)
    
#     print("Middle of linked list ",get_linked_list_middel(head=head))


'''
Q2 : Reverse a Linked List
'''

# Iterative approach 

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        

# def reverse_linked_list(head:Node)->Node:
#     current = head
#     previous = None
    
#     while current:
#         next_node = current.next
        
#         current.next = previous
        
#         previous = current
        
#         current = next_node
    
#     return previous


        

# def traverse_linked_list(head:Node)->None:
#     while head:
#         print(head.data,end=" ")
#         head = head.next     
    


# '''
# tc = O(n)
# sc = O(1)
# '''

# if __name__ == "__main__":
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
    
#     traverse_linked_list(head=reverse_linked_list(head=head))


# Recursive approach

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        

def traverse_linked_list(head:Node)->None:
    
    while head:
        print(head.data,end=" ")
        head = head.next


def reverse_linked_list(head:Node)->Node:
    if head is None or head.next is None:
        return head
    rest = reverse_linked_list(head=head.next)
    head.next.next = head
    head.next = None
    return rest

'''
tc = O(n)
sc = O(n)
'''


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    
    # traverse_linked_list(head=reverse_linked_list(head=head))
    reverse_linked_list(head=head)