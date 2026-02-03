'''
Q1 : Second largest number in an array 
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34

Input: arr[] = [10, 5, 10]
Output: 5

Input: arr[] = [10, 10, 10]
Output: -1
'''
# ++++++++++ Sorting Approach +++++++++++++++++++++
# def second_largest_element(arr:list):
#     n  = len(arr)
#     arr.sort()
#     for i in range(n - 2,-1,-1):
#         if arr[i] != arr[n-1]:
#             return arr[i]
#     return -1


# if __name__ == "__main__":
#     arr = [10, 5, 10]
#     print("Second largest element ",second_largest_element(arr=arr))
    
    
# ++++++++++++ Two Pass Search Approach +++++++++++++++++++++++
# def second_largest_element(arr:list):
#     largest = -1
#     second_largest = -1
#     for elem in arr:
#         if elem > largest:
#             largest = elem
    
#     for elem in arr:
#         if elem < largest and elem > second_largest:
#             second_largest = elem
    
#     return largest,second_largest

# if __name__ == "__main__":
#     arr = [10, 10, 10]
#     _,second_largest = second_largest_element(arr=arr)
#     print("Second largest element in array ",second_largest)
    
# ++++++++++++++ One pass Search approach +++++++++++++++++++++
# def second_largest_element(arr:list):
#     largest = -1
#     second_largest = -1
#     for elem in arr:
#         if elem > largest:
#             second_largest = largest
#             largest = elem
        
#         elif elem < largest and elem > second_largest:
#             second_largest = elem
#     return largest,second_largest

# if __name__ == "__main__":
#     arr = [10, 10, 10]
#     _,second_largest = second_largest_element(arr=arr)
#     print("Second largest element ",second_largest)
    
# ++++++++++++ Recursive Approach ++++++++++++++++++++++++++
def second_largest_element(arr:list,i:int = 0,largest:int=-1,second_largest:int=-1):
    if i == len(arr):
        return largest,second_largest
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] < largest and arr[i] > second_largest:
        second_largest = arr[i]
    return second_largest_element(arr=arr,i= i+1,largest=largest,second_largest=second_largest)

if __name__ == "__main__":
    arr = [10, 10, 10]
    _,second_largest = second_largest_element(arr=arr)
    print("Second largest element ",second_largest)
    
    
