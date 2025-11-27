# Create  Single Linked List class to append, traverse, or insert at kth position


# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None



# class SingleLinkedList:
#     def __init__(self):
#         # Assuming if the node is just created then it will be empty
#         self.head = None
    
    
    
#     def append_linke_list(self,data):
#         new_node = Node(data)
#         # check the head is none
#         if self.head == None:
#             # then append the head value
#             self.head = new_node
#         else:
#             curr  = self.head
#             while curr.next is not None:
#                 curr = curr.next
            
#             curr.next = new_node
     
#     def traverse(self):
#         if self.head is None:
#             print("Singly list empty")
#         else:
#             curr = self.head
#             while curr is not None:
#                 print(curr.data,end=" ")
#                 curr = curr.next
#             print()
            
#     def insert_at(self,val,pos):
#         new_node = Node(val)
        
        
#         if pos == 1:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             curr = self.head
#             prev_node = None
#             count = 1
#             while curr is not None and count < pos:
#                 prev_node = curr
#                 curr = curr.next
#                 count += 1
#             prev_node.next = new_node
#             new_node.next = curr

            


# sll = SingleLinkedList()
# sll.append_linke_list(10)
# sll.append_linke_list(20)
# sll.append_linke_list(30)
# sll.append_linke_list(40)
# sll.append_linke_list(50)

# sll.traverse()
# sll.insert_at(25,3)
# sll.traverse()