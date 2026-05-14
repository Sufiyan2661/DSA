# ++++++++++++++++++++++++++++++++++++++ (24/11/25) Simple array implementation of Queue ++++++++++++++++++++++++++++++++++++++++
class MyQueue:
    def __init__(self,capacity):
        
        
        # Maximum number of elements a queue can store
        self.capacity = capacity
        
        #  Array to store queue elements
        self.arr = [0] * capacity
        
        
        # Current number of elements in the queue
        self.size = 0
        
    
    
    
    # traverse Queue
    def traverse_queue(self):
        if self.size == 0:
            print("Queue is empty can`t perform this operation")
            return
        for i in range(0,self.size):
            print(self.arr[i],end=" ")
        print()
        
    
    # Enqueue (Insert)
    
    def enqueue(self,element):
        ''''
        if number of elements is greater than the capacity then 
        print "Queue is overflowed"
        '''
        if self.size == self.capacity:
            print("Queue Overflowed")
            return
        
        self.arr[self.size] = element
        self.size += 1
        
    # Dequeue () Remove element from the front
    
    def dequeue(self):
        if self.size == 0:
            print("Queue is underflowed")
            return
        elem = self.arr[0]
        for i in range(1,self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1
        return elem
        
        
    # Get front element (peek)
    def get_front(self):
        if self.size == 0:
            print("Queue is empty")
            return -1
        return self.arr[0]
    
    
    # get last element
    def get_rear(self):
        if self.size == 0:
            print("Queue is empty")
            return -1
        return self.arr[self.size -1]
    
    # print element from the given position 
    def get_elem_at_pos(self,pos):
        if pos > self.capacity:
            print("The given position is greater than the total capacity")
            return
        if pos > self.size:
            print("the given position is greater than the totoal size of the elements")
        
        return self.arr[pos]
    
    
    
    
    '''
    check if the queue is empty return true, else false
    '''
    def is_empty(self):
        return self.size == 0
    
    
    '''
    chekc if the queue is full return true , else false
    '''
    def is_full(self):
        return self.size == self.capacity
    
    

if __name__ == "__main__":
    q = MyQueue(3)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    position = 3
    
    print(f"The element at postion {position} is {q.get_elem_at_pos(position)} ")



# +++++++++++++++++++++++++++++++++++ (25/11/25) Implementation of circular queue using array +++++++++++++++++++++++++++++++++++
# class MyQueue:
#     def __init__(self,capacity):
#         # Maximum size of the queue
#         self.capacity = capacity
        
#         # To store the front index of the arr
#         self.front = 0
        
#         # To store the element of the list
#         self.arr = [0] * capacity
        
#         # To Store the current size of queue
#         self.size = 0
        
        
#     '''
#     traverse the elements
#     '''    
#     def traverse_queue(self):
#         if self.size == 0:
#             print("Can`t traverse the empty queue list")
#             return
#         for i in range(0,self.size):
#             print(self.arr[i],end=" ")
#         print()


#     '''
#     enqueue(x) inserting element from the rear
#     '''
    
#     def enqueue(self,element):
#         if self.size == self.capacity:
#             print("Queue is Full")
#             return
#         rear =  (self.front + self.size) % self.capacity
#         self.arr[rear] = element
#         self.size += 1

#     '''
#     dequeue() Remove and return the front element from
#     the circular queue
#     '''
    
#     def dequeue(self):
#         if self.size == 0:
#             print("Queue is empty")
#             return -1 
#         res = self.arr[self.front]
#         self.front = (self.front + 1) % self.capacity
#         self.size -= 1
#         return res
    
    
#     '''
#     getRear() return element from the rear of the circular queue
#     '''
#     def get_rear(self):
#         if self.size == 0:
#             print("Queue is empty")
#             return -1
#         rear = (self.front + self.size -1) % self.capacity
#         return self.arr[rear]
    
    
#     '''
#     getFront() return the first element of the circular queue
#     '''
    
#     def get_front(self):
#         if self.size == 0:
#             print("Queue is empty")
#             return -1
#         return self.arr[self.front]
    


# if __name__ == "__main__":
#     q = MyQueue(3)
#     q.enqueue(10)
#     q.enqueue(20)
#     q.enqueue(30)
#     q.traverse_queue()





# +++++++++++++++++++++++++++++++++++++ (25/11/25) Queue - Linked list Implementation +++++++++++++++++++++++++++++++++++++++++++

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# class MyQueue:
#     def __init__(self):
        
#         # Points to the first node (head of the queue)
#         self.front = None
        
#         # Points to the last node (Tail of the queue)
#         self.rear = None 
        
#         # Current size of the queue
#         self.size = 0
        
    
    
#     '''
#     enqueue(x) :- adds the element at the rear of the queue unlike 
#     array there is no fixed capacity in linked list.
#     '''
#     def enqueue(self,element):
#         new_node = Node(element)
#         if self.front == None and self.rear == None:
#             # self.front = new_node
#             # self.rear = new_node
#             self.front = self.rear = new_node
#         self.rear.next = new_node
#         self.rear = new_node
#         self.size += 1
    
    
#     '''
#     dequeue() :- remove the element from the front of the queue
#     '''
    
#     def dequeue(self):
#         if self.front == 0:
#             print("Queue is Empty")
#             return
#         temp = self.front
#         self.front = self.front.next
#         if self.front is None:
#             self.rear = None
#         self.size -= 1

    
#     '''
#     isEmpty() checks whether the queue has no elements
#     '''
#     def is_empty(self):
#         return self.front is None
    
#     '''
#     frontOperation() returns the element from the front of the queue
#     without removing it.
#     '''
#     def get_front(self):
#         if self.is_empty():
#             print("Queue is empty")
#             return -1
#         return self.front.data
    
    
#     '''
#     getRear() returns the elmenent from the last of the queue 
#     '''
#     def get_rear(self):
#         if self.is_empty():
#             print("Queue is empty")
#             return - 1
#         return self.rear.data 
    
#     '''
#     traverse() traverse the queue 
#     '''
#     def traverse(self):
#         if self.is_empty():
#             print("Queue is empty")
#             return
#         temp = self.front
#         while temp:
#             print(temp.data,end=" ")
#             temp = temp.next
#         print()
        
#     '''
#     size() return the length of the queue
#     '''
#     def get_size(self):
#         if self.is_empty():
#             print("Queue is empty ")
#             return
#         return self.size





# if __name__ == "__main__":
#     q = MyQueue()
    
#     q.enqueue(10)
#     q.enqueue(20)
#     q.enqueue(30)
    
#     # q.dequeue()
    
#     print("The first element from the queue ",q.get_front())
#     print("The last element from the queue ",q.get_rear())
    
#     print("The length of the queue ",q.get_size())

    
#     q.traverse()

