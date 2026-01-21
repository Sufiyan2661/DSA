# (1) ++++++++++++++++++++++++++++++++ Alternate Elements of An Array ++++++++++++++++++++++++++++++++
# input = [10,20,30,40,50]
# output = [10,30,50]

# arr = [-5, 1, 4, 2, 12]
# new_arr = []
# for i in range(0,len(arr),2):
#     new_arr.append(arr[i])

# print(new_arr)


# (2) ++++++++++++++++++++++++++++++++++++++ Leaders in an array ++++++++++++++++++++++++++++++++++++++
# Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.
# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]

# NAIVE APPROACH

# def leaders(arr):
#     new_arr = []
#     n = len(arr)
#     for i in range(n):
        
#         # check elements to the right 
#         for j in range(i + 1,n):
            
            
            
#             if arr[i]<arr[j]:
#                 break
#         else:
#             new_arr.append(arr[i])
    
    
#     return new_arr


# if __name__ == "__main__":
#     arr = [16, 17, 4, 3, 5, 2]
#     result = leaders(arr)
#     print(" ".join(map(str, result)))



# Expected Approach


# def leader(arr=[]):
#     new_arr = []
#     n = len(arr)
    
#     max_right = arr[-1]
    
    
#     # last element is always the leader
    
#     new_arr.append(max_right)
    
#     # start from the last element
#     for i in range(n - 2,-1,-1):
#         print(arr[i])
#         if arr[i] >= max_right:
#             max_right = arr[i]
#             new_arr.append(max_right)
            
            
#     new_arr.reverse()
    
#     return new_arr


# if __name__ == "__main__":
#     arr = [16, 17, 4, 3, 5, 2]
#     result = leader(arr)
#     print("Result ",result)



# (3) +++++++++++++++++++++++++++++++++++ Check if an Array is Sorted +++++++++++++++++++++++++++++++++++
# Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.
# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true

# APPROACH 1
# def checksorted(arr):
#     n = len(arr)
#     if n == 0 or n == 1:
#         return
    
#     for i in range(1,n):
#         if arr[i -1] > arr[i]:
#             return False
        
#     return True


# APPROACH 2 
# def checksorted(arr):
#     return arr == sorted(arr)



# APPROACH RECURSIVE
# def is_sorted_helper(arr,n):
    
#     if n == 0 or n == 1:
#         return True
    
#     return (arr[n -1] >= arr[n - 2] and is_sorted_helper(arr,n-1))
# def checksorted(arr):
#     n = len(arr)
    
#     return is_sorted_helper(arr,n)
# if __name__ == "__main__":
#     arr = [10, 20, 30, 40, 50]
#     print("Is Sorted ",checksorted(arr))
    
    

# (4) ++++++++++++++++++++++++++++++++++ Remove Duplicates From Sorted ++++++++++++++++++++++++++++++++++ 
# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

# def remove_duplicates(arr):
#     seen = set()
    
#     idx = 0
    
#     for i in range(len(arr)):
#         if arr[i] not in seen:
#             seen.add(arr[i])
#             arr[idx] = arr[i]
#             idx += 1
            
#     return idx

# def remove_duplicates(arr):
#     n = len(arr)
#     new_arr = []
#     for i in range(len(arr)):
#         if arr[i] not in new_arr:
#             new_arr.append(arr[i])
#     return new_arr


# if __name__ == "__main__":
#     arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
#     print("Removed ",remove_duplicates(arr))

# (5) ++++++++++++++++++++++++++++++++++ Generating All Subarrays ++++++++++++++++++++++++++++++++++
# Given an array arr[], the task is to generate all the possible subarrays of the given array.
# ITERATIVE APPROACH

# def sub_arrays(arr):
#     n = len(arr)
    
#     for i in range(n):
#         # print(arr[i]) 
#         for j in range(i , n):
#             for k in range(i,j+1):
#                 print(arr[k],end=" ")
#             print()
# if __name__ == "__main__":
#     arr = [1,2,3,4]
#     sub_arrays(arr)




# +++++++++++++++++++++++++++++++++++++++++++ Array Reverse +++++++++++++++++++++++++++++++++++++++++++

# Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.
# ITERATIVE APPROACH

# def reverse_array(arr):
#     # length of the arr
#     n = len(arr)
    
    
#     # copying the lenght of the original array
#     temp = [0] * n
    
    
#     # tempararly copying the array
#     for i in range(n):
#         temp[i] = arr[n - i -1]
        
#     # copying back to the original array
    
    
#     for i in range(n):
#         arr[i] = temp[i]
#     return arr

        
# def reverse_array(arr):
#     # length of the array
#     n = len(arr)
#     left_pointer = 0
#     right_pointer = n - 1
    
    
#     # check till left pointer is less than right pointer
#     while left_pointer < right_pointer:
#         arr[left_pointer],arr[right_pointer] = arr[right_pointer],arr[left_pointer]

        
#         right_pointer -= 1
#         left_pointer += 1
#     return arr
    


# USING BUILT IN METHODS

# def reverse_array(arr):
#     arr.reverse()
#     return arr
# if __name__ == "__main__":
#     arr = [1, 4, 3, 2, 6, 5]  
#     result = reverse_array(arr)
#     print("Reversed Array ",result)


# MY APPROACH
# def reverse_array(arr):
#     n = len(arr)
#     new_array = []
#     for i in range(n-1,-1,-1):
#         new_array.append(arr[i])
#     return new_array


# if __name__ == "__main__":
#     arr = [1,3,4,5,6,9]
#     result = reverse_array(arr)
#     print("Reversed Array",result)