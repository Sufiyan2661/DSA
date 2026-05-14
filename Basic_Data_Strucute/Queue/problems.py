
class Queue:
    def __init__(self,capacity):
        self.capacity = capacity
        
        self.arr = [0] * capacity
        
        
        self.size = 0
        
    
    
    def is_full(self):
        return self.size == self.capacity
    
    def get_size(self):
        return self.size
    
    def enqueue(self,data):
        if self.capacity == self.size:
            print("Queue is overflowing")
            return
        self.arr[self.size] = data
        self.size += 1
        
    
    def traverse(self):
        if self.size == 0:
            print("Can`t perform this operation Queue is empty")
            return
        for i in range(self.size):
            print(self.arr[i],end=" ")
        print()
        
    def dequeue(self):
        if self.size == 0:
            print('Cant perform this opertion Queue is empty')
            return
        elem = self.arr[0]
        for i in range(1,self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1
        return elem
    
        
        
        
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    
    
    q.traverse()
    print("first element ",q.dequeue())
    print("first element ",q.dequeue())
    print("first element ",q.dequeue())
    print("first element ",q.dequeue())
    print("first element ",q.dequeue())
    print("first element ",q.dequeue())
    
        