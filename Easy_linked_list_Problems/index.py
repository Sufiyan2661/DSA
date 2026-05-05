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
tc  = O(n)
sc = O(1)
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

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        

# def traverse_linked_list(head:Node)->None:
    
#     while head:
#         print(head.data,end=" ")
#         head = head.next


# def reverse_linked_list(head:Node)->Node:
#     if head is None or head.next is None:
#         return head
#     rest = reverse_linked_list(head=head.next)
#     head.next.next = head
#     head.next = None
#     return rest

# '''
# tc = O(n)
# sc = O(n)
# '''


# if __name__ == "__main__":
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
    
#     # traverse_linked_list(head=reverse_linked_list(head=head))
#     reverse_linked_list(head=head)


'''
Q3 : Remove every k-th node of the linked list
Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
Output: 1 -> 3 -> 5 
Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 .

Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.
'''

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        

# def print_node(head):
#     while head:
#         print(head.data,end=" ")
#         head = head.next


# def remove_kth_nodes(head,k):
    
#     if head is None or k <= 0:
#         return head
    
#     current = head
#     previous = None
#     count = 1
    
#     while current:
        
#         if count == k:
            
            
#             if previous is None:
#                 head = current.next
                
#                 current = head
#             else:
                
#                 previous.next = current.next
#                 current = current.next
#             count = 1
        
#         else:
            
#             previous = current
#             current = current.next
#             count = count + 1
#     return head

'''
tc = O(n)
sc = O(1)
'''

# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     head.next.next.next.next.next = Node(6)
#     print_node(head)
#     print("\n")
#     remove_kth_nodes(head,2)
#     print_node(head)
        
'''
Q4 : Insertion in linked list
'''

# Insertion at front

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None



# def print_list(head):
#     curr = head
#     while curr:
#         print(curr.data,end="")
#         if curr.next:
#             print(" ---> ",end=" ")
#         curr = curr.next
#     print("\n")

# def insert_at_front(head,data):
#     new_node = Node(data)
#     new_node.next = head
#     return new_node


# def insert_node_after_given_node(head,g,data):
#     curr = head
    
#     while curr:
#         if curr.data == g:
#             break
#         curr = curr.next
        
#     if curr is None:
#         return 
    
    
#     new_node = Node(data)
    
#     new_node.next = curr.next        
#     curr.next = new_node
#     return head
        

# if __name__ == "__main__":
#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)
#     # print_list(head)
#     head = insert_at_front(head,1)
#     # print_list(head)
#     # head = insert_at_front(head,0)
#     head = insert_node_after_given_node(head,5,6)
#     print_list(head)


'''
Q5 : Reverse doubly linked list

'''

# Naive approach (recursive)
# class Node():
    
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None

# def reverse_dll(curr):
    
#     if curr is None:
#         return None
    
#     temp = curr.prev
#     curr.prev = curr.next
#     curr.next = temp
    
    
#     if curr.prev is None:
#         return curr
    
#     return reverse_dll(curr.prev)





# def print_dll(head):
#     curr = head 
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next is not None:
#             print(" <--> ",end="")
#         curr = curr.next
#     print()
    

# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.prev = head
#     head.next.next = Node(3)
#     head.next.next.prev = head.next
    
#     print_dll(head=head)
#     curr = head
#     curr = reverse_dll(curr)
#     print_dll(curr)


# Expected approach Using two pointers


# class Node():
    
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
        


# def reverse_dll(head):
    
    
#     if head is None or head.next is None:
#         return head
#     prev_node = None
    
#     curr = head
    
#     while curr is not None:
        
#         prev_node = curr.prev
        
#         curr.prev = curr.next
        
#         curr.next = prev_node
        
        
#         curr = curr.prev
        
    
#     return prev_node.prev


    

# def print_dll(head):
#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next is not None:
#             print(" <--> ",end=" ")
#         curr = curr.next
#     print()


# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.prev = head
#     head.next.next = Node(3)
#     head.next.next.prev = head.next
    
#     print_dll(head=head)    
#     head = reverse_dll(head=head)
#     print_dll(head=head)

'''
Q 6 : Rotate Linked List

k = 4
10 -> 20 -> 30 -> 40 -> 50
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
def print_ll(head):
    curr = head 
    while curr:
        print(curr.data,end=" ")
        if curr.next is not None:
            print("--> ",end=" ")
    
        curr = curr.next
    print()
    
    
# def rotate_by_k(head,k):
    
#     if not head or k == 0:
#         return head

#     curr = head
    
#     # step 1 find the lenght of linked list
#     lenght = 1
#     while curr.next:
#         curr = curr.next 
#         lenght += 1
        
#     last = curr
        
#     print("lenght ",lenght)

#     # Step two normalize k 
#     k = k % lenght

#     # Step 3 move to k - 1
    
#     if k == 0:
#         return head
    
    
#     curr = head
#     for _ in range(k -1):
        
#         curr = curr.next
        
    
#     new_head = curr.next
    
    
#     # step 4 rotate
#     curr.next = None
#     last.next = head
    
#     return new_head

        

# '''
# tc = O(n)
# sc =  O(1)
# '''

        

# if __name__ == "__main__":
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
#     print_ll(head=head)
#     new_head = rotate_by_k(head=head,k=4)
#     print_ll(head=new_head)
    


# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def print_ll(head):
#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next is not None:
#             print(" --> ",end=" ")
#         curr =  curr.next
#     print()
    
# def rotate_by_k(head,k):
    
#     if not head or k == 0:
#         return head
    
#     curr = head    
#     for _ in range(k - 1):
        
#         while curr.next is not None:
#             curr = curr.next
            
#         curr.next = head
#         curr = curr.next
        
#         head = head.next
        
#         curr.next = None
        
#     return head
        

# if __name__ == "__main__":
    
    # head = Node(10)
    # head.next = Node(20)
    # head.next.next = Node(30)
    # head.next.next.next = Node(40)
    # head.next.next.next.next = Node(50)
    
#     print_ll(head)
#     new_head = rotate_by_k(head,4)
#     print_ll(head)
    
'''
Q 7 : kth from the end of a Linked List
Input: head=1 -> 2 -> 3 -> 4, k= 3
Output: 2
Explanation: Node 2 is the third node from the end of the linked list.

Input: head=35 -> 15 -> 4 -> 20, k = 5
Output: -1
Explanation: length of linked list is less then  k so  -1. 
'''

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    

# def print_ll(head):
#     current = head
#     while current:
#         print(current.data,end=" ")
#         if current.next is not None:
#             print(" --> ",end=" ")
#         current = current.next
#     print()


# def kth_node_from_last(head,k):
    
#     current = head
#     length = 1
#     while current.next is not None:
#         current = current.next
#         length = length + 1
        
#     if k > length:
#         return -1
#     current = head
#     for _ in range(1,(length - k) + 1):
#         print()
#         current = current.next
        
    
#     return current.data
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
    
#     print_ll(head=head)
#     node = kth_node_from_last(head,3)
#     print("kth node ",node)


# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    

# def print_ll(head):
#     current = head
#     while current:
#         print(current.data,end=" ")
#         if current.next is not None:
#             print(" --> ",end=" ")
#         current = current.next
#     print()

# def kth_from_last(head,k):
    
#     main_ptr = head
#     ref_ptr = head
    
#     for _ in range(1,k):
#         ref_ptr  = ref_ptr.next
        
    
#     if ref_ptr.next is None:
#         return -1
    
    
#     while ref_ptr.next is not None:
#         ref_ptr = ref_ptr.next
#         main_ptr = main_ptr.next
    
    
#     return main_ptr.data    
    


# if __name__ == "__main__":
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
    
#     node = kth_from_last(head,3)
#     print("The kth node ",node)





class Node():
    def __init__(self,data = 0):
        self.data = data
        self.next = None





def add_two_numbers(l1:Node,l2:Node) -> Node:
    dummy = Node()
    
    current = dummy
    
    carry = 0
    
    while l1 is not None or l2 is not None or carry != 0:
        
        
        _sum = carry
        
        
        if l1 is not None:
            _sum = _sum + l1.data
            l1 = l1.next
        
        if l2 is not None:
            _sum = _sum + l2.data
            l2 = l2.next
        
        
        carry = _sum // 10
        
        digit = _sum % 10
        
        new_node = Node(digit)
        
        current.next = new_node
        current = current.next
        
    return dummy.next

def print_ll(head):
    curr = head
    while curr:
        print(curr.data,end=" ")
        if curr.next:
            print(" --> ",end=" ")
        curr = curr.next
    print()
    



if __name__ == "__main__":
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)
    
    print("List One ",end=" ")
    print_ll(l1)
    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)
    
    print("List Two ",end=" ")
    print_ll(l2)
    
    
    l3 = add_two_numbers(l1,l2)
    print("List three ")
    print_ll(l3)
    
    
    