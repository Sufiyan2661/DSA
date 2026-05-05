# Creating an example of linked list of size 3
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# # Create the first Node
# head = Node(10)


# # Link the second Node
# head.next = Node(20)


# # Link the third Node
# head.next.next = Node(30)


# # Link the fourth Node
# head.next.next.next = Node(40)

# Printing the linked list

# temp = head
# while temp is not None:
#     print(temp.data,end=" ")
#     temp = temp.next

# +++++++++++++++++++++++++++++++++++ Common operation in Linked List +++++++++++++++++++++++++++++++++++

# (1)  Traverse of singly linked list
# Iterative Approach
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def traverse_linked_list(head):
#     while head is not None:
#         print(head.data,end=" ")
#         if head.next is not None:
#             print("->",end=" ")
#         head = head.next

# # Calling the function
# if __name__ == "__main__":
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
#     head.next.next.next.next.next = Node(60)

#     traverse_linked_list(head)


# Recursive Approach

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def traverse_linked_list(head):
#     if head is None:
#         print()
#         return


#     print(head.data,end=" ")

#     if head.next is not None:
#         print("-->",end=" ")


#     traverse_linked_list(head.next)


# if __name__ == "__main__":
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)
#     head.next.next.next.next = Node(50)
#     head.next.next.next.next.next = Node(60)

#     traverse_linked_list(head)

# (2) Insertion


# (i) Inert at the begining of the linked list
# input x = 1
# output = 1 -> 2 -> 3 -> 4 -> 5

# class Node:
#     def __init__(self,x):
#         self.data = x
#         self.next = None

# Fucntion to insert a new Node at the begining of the list
# def insert_at_front(head,x):
#     new_node = Node(x)
#     new_node.next = head
#     return new_node

# # function to print the contents of the linked list
# def print_list(head):
#     current = head
#     while current is not None:
#         print(current.data,end=" ")
#         if current.next is not None:
#             print("-->",end=" ")
#         current = current.next
#     print()


# if __name__ == "__main__":
#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)

#     x = 1
#     head = insert_at_front(head,x)
#     print_list(head)


# INSERT NODE AT THE END OF THE LINKED LIST
# Given a head of the linked list , we need to insert a new node at the end of the linked list

# input  x = 6
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# create new node and set its next pointer as NULL since it will be the last node
# class Node:
#     def __init__(self,x):
#         self.data = x
#         self.next = None


# Given a head of the list and an int, appends the new node appends the head and returns the head
# def insert_at_last(head,x):
#     new_node = Node(x)


#     # if the linked list is empty, make the head as the new node and return
#     if head is None:
#         return new_node

#     # Store the head reference in the temporary variable
#     temp = head

#     # traverse till the last node
#     while temp.next is not None:
#         temp = temp.next


#     # Change the next pointer of the last node to point to the new node
#     temp.next = new_node


#     # return the head of the list
#     return head


# def print_list(head):
#     current = head
#     while current is not None:
#         print(current.data,end=" ")
#         if current.next is not None:
#             print("-->",end=" ")
#         current = current.next
#     print()


# if __name__ == "__main__":
#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)

#     x = 1
#     head = insert_at_last(head,x)
#     print_list(head)


# INSERT NODE AT THE SPECIFIC POSITION
# Given a head of singly linked list, a position pos, and val, Insert that data into a linked list at the given position.

# Creating Node
# class Node:
#     def __init__(self,x):
#         self.data = x
#         self.next = None


# def insert_at_position(head,pos,val):

#     if pos < 1:
#         return head


#     # head will change if the pos == 1
#     if pos == 1:
#         new_node = Node(val)
#         new_node.next = head
#         return new_node

#     curr = head

#     # Traverse the node just before the new node

#     for i in range(1,pos -1):
#         if curr is None:
#             return head
#         curr = curr.next


#     # if position is greater than the number of nodes
#     if curr is None:
#         return head

#     new_node = Node(val)


#     new_node.next = curr.next
#     curr.next = new_node

#     return head


# def print_linked_list(head):
#     curr = head
#     while curr is not None:
#         print(curr.data,end=" ")
#         if curr.next is not None:
#             print("-->",end=" ")
#         curr = curr.next
#     print()


# if __name__ == "__main__":
#     # creating the list  1,2,4

#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(4)

#     val, pos = 3, 3

#     head = insert_at_position(head,pos,val)

#     print_linked_list(head)

#
#                                              # (3) Deletion

#  DELETION AT BEGINNNING (REMOVAL OF FIRST NODE) IN A LINKED LIST
# Given the head of the linked list ,we need to remove the first node from the given linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def delete_first_node(head):
#     if head is None:
#         return

#     temp = head

#     head = head.next

#     temp = None

#     return head


# # print linked list
# def print_linked_list(curr):
#     while curr is not None:
#         print(curr.data,end=" ")
#         if curr.next is not None:
#             print("-->",end=" ")
#         curr = curr.next
#     print()


# if __name__ == "__main__":


#     head = Node(8)
#     head.next = Node(6)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)
#     head.next.next.next.next = Node(3)


#     head = delete_first_node(head)
#     print_linked_list(head)


# DELETION AT END (REMOVAL OF LAST NODE) IN A LINKED LIST
# Given the head of the list remove the last node


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def delete_node_at_end(head):
#     # Check if the list is empty
#     if head is None:
#         return None

#     # Check the list has only one node
#     if head.next is None:
#         return None

#     # Find the second last node
#     second_last = head.next

#     while second_last.next.next is not None:
#         second_last = second_last.next


#     # delete the last node by making second last point to None

#     second_last.next = None

#     return head


# def print_linked_list(head):
#     while head is not None:
#         print(head.data,end=" ")
#         if head.next is not None:
#             print(" --> ",end=" ")
#         head = head.next
#     print()


# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)


#     head = delete_node_at_end(head)
#     print_linked_list(head=head)


# DELETE NODE BY POSITION

# Given the head of singly linked list and a position (1 - based index), delete the node at the position and return the updated head of the linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def delete_at_position(head,position):
#     temp = head

#     if position == 1:
#         head = head.next
#         return head

#     # Traverse to the node before the one to be deleted
#     prev = None

#     for i in range(1,position):
#         prev = temp
#         temp = temp.next


#     prev.next = temp.next
#     return head


# def print_linked_list(head):
#     while head is not None:
#         print(head.data,end=" ")
#         if head.next is not None:
#             print("-->",end=" ")
#         head = head.next
#     print()


# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(5)
#     head.next.next = Node(4)
#     head.next.next.next = Node(8)
#     head.next.next.next.next = Node(3)

#     head = delete_at_position(head,2)

#     print_linked_list(head)


# ++++++++++++++++++++++++++++++++++++++++++++++++      ++++++++++++++++++++++++++++++++++++++++++++
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.print_nodes()
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            self.print_nodes()

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.print_nodes()

    def add_node_at_position(self, position, data):
        new_node = Node(data)
        if self.head is None:
            if position == 1:
                self.add_node(data)
                self.print_nodes()
                return
            else:
                print("Can`t perform this operation on empty list")

        if position == 1:
            self.add_node(data)
            return

        current_node = self.head
        previous_node = None
        count = 1
        while current_node and count < position:
            previous_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            print("Position out of bound")
            return

        previous_node.next = new_node
        new_node.next = current_node
        self.print_nodes()

    def remove_first_node(self):
        if self.head is None:
            print("Can`t perform this operation on empty list")
        else:
            # Get the first Node
            first_node = self.head

            self.head = first_node.next
            self.print_nodes()

    def remove_last_node(self):
        if self.head is None:
            print("Can`t perform this operation on empty list")
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None
            self.print_nodes()

    def remove_node_at_position(self, position):
        if self.head is None:
            print("Can`t perform this operation on empty list")

        if position == 1:
            self.remove_first_node()
            return

        current_node = self.head
        previous_node = None
        count = 1
        while current_node and count < position:
            previous_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            print("Postion is out of bound")
            return
        previous_node.next = current_node.next
        self.print_nodes()

    def print_nodes(self):
        if self.head is None:
            print("Nothing is here")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data, end=" ")
                if current_node.next is not None:
                    print("-->", end=" ")
                current_node = current_node.next
            print()

    def reverse_list(self):
        if self.head is None:
            print("Can`t perform this operation on empty list")
            return
        else:
            # initialize three pointers
            previous_node = None
            current_node = self.head
            next_node = None

            while current_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            self.head = previous_node
            self.print_nodes()

    def maximum_from(self):
        if self.head is None:
            print("Can`t perform this operation on empty list")
            return
        else:
            current_node = self.head
            lowest_value = 0
            while current_node:
                if current_node.data > lowest_value:
                    lowest_value = current_node.data
                current_node = current_node.next
            print("Maximum value from the node is ", lowest_value)

    def list_len(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        print(count)


# if __name__ == "__main__":
#     sll  = SinglyLinkedList()
#     sll.append_node(30)
#     sll.append_node(40)
#     sll.append_node(10)
#     sll.append_node(20)
# sll.reverse_list()
# sll.add_node(4)
# # sll.remove_first_node()
# # sll.remove_last_node()
# sll.add_node_at_position(5,35)
# # sll.remove_node_at_position(2)

# sll.print_nodes()
# sll.reverse_list()
# sll.maximum_from()
# sll.list_len()

# +++++++++++++++++++++++=========================++++++++++++++++++++++++================================
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# ++++++++++++++++++++++++++++++++++ DOUBLY LINKED LIST ++++++++++++++++++++++++++++++++++++++++++++++++++++
# class Node:
#     def __init__(self,data):
#         self.data = data

#         self.prev = None

#         self.next = None


# def insert_at_front(head,data):

#     # create a new node
#     new_node = Node(data)


#     # Make next of new node as head
#     new_node.next = head


#     # change prev of head node to new node
#     if head is not None:
#         head.prev = new_node

#     # Return the new node as the head of the doubly linked list
#     return new_node

# # Fucntion to insert the new node at the end of the linked list
# def insert_at_end(head,data):

#     # Create new node
#     new_node = Node(data)


#     # If the linked list is empty, set the new node as the head
#     if head is None:
#         head = new_node
#     else:
#         current_node = head
#         while current_node.next:
#             current_node = current_node.next
#         # set the next node of the last node to the new node
#         current_node.next = new_node

#         new_node.prev  = current_node

#     return head

# # Function to insert the node at the given positon
# def insert_at_position(head,position,data):


#     # create new node
#     new_node = Node(data)

#     # insert at the beginning
#     if position == 1:
#         new_node.next = head


#         # if the linked list is not empty set the previous pointer of head to new_node
#         if head is not None:
#             head.prev = new_node


#         # set the new node as the head of the linked list
#         head = new_node
#         return new_node

#     current = head

#     for _ in range(1,position - 1):
#         if current is None:
#             print("position is out of bound")
#             return head
#         current = current.next

#     # If the position is out of bounds
#     if current is None:
#         print("Postion is out of bounds")
#         return head

#     # set the previous pointer of new node to current
#     new_node.prev = current

#     # set the next of new node to next of current
#     new_node.next = current.next


#     # Update the next of current node to new node
#     current.next = new_node

#     # if the new node is not the last node, update previous pointer of next node to new node
#     if new_node.next is not None:
#         new_node.next.prev = new_node

#     return head


# def delete_head(head):

#     # if Empty return None
#     if head is None:
#         return None

#     # Store in temp for deletion later
#     temp = head

#     # Move head to the next node
#     head = head.next


#     # Set previous pointer of the head
#     if head is not None:
#         head.prev = None

#     # Return new head

#     return head


# def delete_last(head):
#     # Corner cases
#     if head is None or head.next is None:
#         return None

#     # Traverse to the last node
#     curr = head
#     while curr.next is not None:
#         curr = curr.next

#     # Disconnect the last node
#     prev_node = curr.prev
#     if prev_node:
#         prev_node.next = None
#         curr.prev = None  # Optional: clean up the removed node's pointer


#     return head

# def delete_at_position(head, position):
#     if head is None:
#         return None

#     current = head

#     # Traverse to the node at the given position
#     for i in range(1, position):
#         if current is None:
#             return head  # Position exceeds list length
#         current = current.next

#     if current is None:
#         return head  # Position exceeds list length

#     # Update next node's prev pointer
#     if current.next is not None:
#         current.next.prev = current.prev

#     # Update previous node's next pointer
#     if current.prev is not None:
#         current.prev.next = current.next
#     else:
#         # If deleting the head
#         head = current.next

#     del current
#     return head

# def print_list(head):
#     current_node = head
#     while current_node:
#         print(current_node.data,end=" ")
#         current_node = current_node.next
#     print()


# if __name__ == "__main__":
#     head = Node(10)
#     second = Node(20)
#     third = Node(30)
#     fourth = Node(40)


#     head.next = second
#     second.prev = head
#     second.next = third
#     third.prev = second
#     third.next = fourth
#     fourth.prev = third


#     # print the original linked list
#     print("Original linked list ",end=" ")
#     print_list(head)


#     # Insert a new node at the front of the list
#     # print("After inserting node at the front ",end=" ")
#     # data = 5
#     # head = insert_at_front(head,data)

#     # print updated list
#     # print_list(head)


#     # Insert new node at the end of the list

#     # print("After inserting node at the end ",end=" ")
#     # data = 45
#     # head = insert_at_end(head,data)


#     # print updated list
#     # print_list(head)


#     # Insert at the given position
#     # data = 35
#     # position = 4
#     # print(f"inserting new_node {data} to the given position => {position}")
#     # head = insert_at_position(head,position,data)


#     # print updated list
#     # print_list(head)


#     # Delete node
#     # head = delete_head(head)


#     # print after deletion
#     # print_list(head)


#     # Delete last node
#     # new_head = delete_last(head)

#     # Delete node at specific position
#     head = delete_at_position(head,3)

#     # print after deletion
#     print_list(head)

# class Node:
#     def __init__(self,data):
#         self.data = data
        
#         # Previous pointer
#         self.prev = None
        
#         # Next Pointer
#         self.next = None
        

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

    
    
#     def add_node(self,data):
#         new_node = Node(data)
        
#         # Make next pointer of new node as head
#         new_node.next = self.head
        
#         # Change previous pointer of head node to new node
#         if self.head is not None:
#             self.head.prev = new_node
#         self.head = new_node
    
    
#     def append_node(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.add_node(data)
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next
            
#             # set the next of the last node to the new node
#             current_node.next = new_node

#             # set previous pointer of the new node to the last node
#             new_node.prev = current_node

#     def insert_at_position(self,position,data):
#         # Create new node 
#         new_node = Node(data)
        
#         # Insertion at the beginning
#         if position == 1:
#             new_node.next = self.head
            
#             # If the linked list is not empty, set the previous pointer of head to new node
#             if self.head is not None:
#                 self.head.prev = new_node
            
#             # set the new node as the head of the linked list
#             self.head = new_node
        
        
#         current_node = self.head
        
#         # Traverse the list to find the node before the insertion point
#         for _ in range(1,position - 1):
#             if current_node is None:
#                 print("Position is out of bounds.")
#                 return
#             current_node = current_node.next
#         # if the position is out of bound
#         if current_node is None:
#             print("Position is out of bounds.")
#             return
        
#         # set previous pointer of new node to current
#         new_node.prev = current_node
        
#         # set the next pointer of new node to next pointer of current node
#         new_node.next = current_node.next
        
        
#         # update the next pointer of current node to new node
#         current_node.next = new_node
        
#         # If the new node is not the last node, update previous pointer of next node to new node
#         if new_node.next is not None:
#             new_node.next.prev = new_node
            
#     def delete_from_beginning(self):
#         if self.head is None:
#             print("Can`t perform this operation on empty linked list.")
#         else:
#             # store it in temprary variable for later deletion
#             temp = self.head
            
            
#             # Move head to the next node
#             self.head = self.head.next

            
#             # set previous pointer of the new head
#             if self.head is not None:
#                 self.head.prev = None
#             del temp
    
#     def delete_from_end(self):
#         if self.head is None:
#             print("Can`t perform this operation on empty linked list.")
#         else:
#             current_node = self.head
#             # traverse to the last node
#             while current_node.next:
#                 current_node = current_node.next

#             # Update the previous node`s next pointer
#             if current_node.prev is not None:
#                 current_node.prev.next = None
                
        
#     def traverse_list(self):
#         if self.head is None:
#             print("Can`t perform this operation empty linked list")
#         else:
#             current_node = self.head
#             while current_node:
#                 print(current_node.data,end=" ")
#                 if current_node.next:
#                     print("<-->",end=" ")
#                 current_node = current_node.next
#             print()





# if __name__ == "__main__":
#     dll = DoublyLinkedList()
#     dll.append_node(10)
#     dll.append_node(20)
#     dll.append_node(30)
#     dll.append_node(40)
#     # dll.insert_at_position(4,35)
#     # dll.delete_from_beginning()
#     dll.delete_from_end()

#     dll.traverse_list()
            
            
            
            
            
            
            
            
# +++++++++++++++++++++++++++++++++++++++++++++== CIRCULAR SINGLY LINKED LIST ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        



def insert_at_beginning(last,data):
    # create new node 
    new_node = Node(data)
    if not last:
        new_node.next = new_node
        return new_node
    
    new_node.next = last.next
    last.next = new_node
    
    return last


def print_list(last):
    if not last:
        return 
    
    head = last.next
    temp = head
    
    while True:
        print(temp.data,end=" ")
        temp = temp.next
        if temp != head:
            print("-->",end=" ")
        else:
            break
    print()
    
    
if __name__ == "__main__":
        
    first = Node(10)
    first.next = Node(20)
    first.next.next = Node(30)
    
    last = first.next.next

    # inset 5 at the beginning 
    last = insert_at_beginning(last,5)
    
    # print list
    
    print_list(last)

