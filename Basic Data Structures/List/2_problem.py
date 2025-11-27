# THIRD LARGEST ELEMENT IN AN ARRAY OF DISTINCT ELEMENTS

# Given an array of integers, the task is to find the third largest element.All the elements in the array are distinct integers.


# Examples:
# input = {1,14,2,16,10,20}
# output = 14
# input = {19,-10,20,14,2,16,10}
# output = 16


# Naive Approach (Sorting)

# def getThirdLargestElement(arr):
    
#     n = len(arr)
    
    
#     arr.sort()
    
#     return arr[n-3]



# Expected Approach (Using three loops)

# def getThirdLargestElement(arr):
    
#     n = len(arr)
    
#     largest = -1
#     secondLargest = -1
#     thirdLargest = -1
    
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
    
    
#     for i in range(n):
#         if arr[i] > secondLargest and arr[i] < largest:
#             secondLargest = arr[i]
        
#     for i in range(n):
#         if arr[i] > thirdLargest and arr[i] < secondLargest:
#             thirdLargest = arr[i]
    
    
#     return thirdLargest
    



# Expected Approach 2 (Using Three variables)

def getThirdLargestElement(arr):
    n = len(arr)
    
    
    largest = -1
    secondLargest = -1
    thirdLargest = -1
    
    
    for i in range(n):
        if arr[i] > largest:
            thirdLargest = secondLargest
            secondLargest = largest
            largest = arr[i]
            
            
        elif arr[i] > secondLargest:
            thirdLargest = secondLargest
            secondLargest = arr[i]
        
        elif arr[i] > thirdLargest:
            thirdLargest = arr[i]
            
    
    
    return thirdLargest
    
    
    

if __name__ == '__main__':
    # arr = [1,14,2,16,10,20]
    arr = [19,-10,20,14,2,16,10]
    print(getThirdLargestElement(arr))