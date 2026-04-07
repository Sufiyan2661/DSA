'''
Q1 Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.
Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
'''

# Iterative approach 

# def is_sorted(arr:list)->bool:
#     n = len(arr)

#     for i in range(1,n):
#         if arr[i] < arr[i - 1]:
#             return False
    
    
#     return True


# Recursive approach

# def is_sorted(arr:list,n:int)->bool:
#     if n == 0 or n == 1:
#         return True
    
#     return arr[n - 1] >= arr[n - 2] and is_sorted(arr,n-1)


# using built in methods 

# def is_sorted(arr:list) -> bool:
#     return arr == sorted(arr)


# if __name__ == "__main__":
#     arr = [10, 20, 30, 40, 50]
#     print("Is Sorted ",is_sorted(arr=arr))


'''
Q2 : Sort a Binary Array
Input :  arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output : arr[] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

Input :  arr[] = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1] 
Output : arr[] = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1] 
'''
# def sort_zero_and_ones(arr:list) -> list:
    
#     lo = 0
#     hi = len(arr) - 1
    
#     while lo < hi:
        
#         while arr[lo] == 0 and lo < hi:
#             lo += 1
        
#         while arr[hi] == 1 and lo < hi:
#             hi -= 1
        
#         if lo < hi:
#             arr[lo],arr[hi] = arr[hi],arr[lo]
#             lo += 1
#             hi -= 1
#     return arr


# if __name__ == "__main__":
#     arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
#     print("Sorted array ",sort_zero_and_ones(arr=arr))



# def sort_zero_and_one(arr:list) ->list:
#     ones = 0
#     zeros = 0
#     new_arr = []
    
#     for elem in arr:
#         if elem == 1:
#             ones += 1
#         else:
#             zeros += 1
    
#     for zero in range(zeros):
#         new_arr.append(0)
    
#     for one in range(ones):
#         new_arr.append(1)
    
#     return new_arr

# if __name__ == "__main__":
#     arr = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
#     print("Sorted Array ",sort_zero_and_one(arr=arr))



'''
Q3: Move all zeros to end of array
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: arr[] = [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: arr[] = [0, 0]
Explanation: No change in array as there are all 0s.
'''

# def move_zeros_to_end(arr:list) -> list:
#     n = len(arr)
#     new_arr = [0] * n
#     i = 0
#     for elem in arr:
#         if elem != 0:
#             new_arr[i]= elem
#             i += 1

    
#     return new_arr
    

# if __name__ == "__main__":
#     arr = [1, 2, 0, 4, 3, 0, 5, 0]
#     print("Sorted Array ",move_zeros_to_end(arr=arr))



# def move_zeros_to_end(arr:list) -> list:
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[count] = arr[i]
#             count += 1
    
#     for i in range(count,len(arr)):
#         arr[i] = 0
    
#     return arr


# if __name__ == "__main__":
#     arr = [1, 2, 0, 4, 3, 0, 5, 0]
#     print("Sorted Array ",move_zeros_to_end(arr=arr))




'''
Q4 : Separate Negative and Positive Numbers
Input: arr[] = [12, 11, -13, -5, 6, -7, 5, -3, -6]
Output: [-13, -5, -7, -3, -6, 12, 11, 6, 5]
Explanation: All negative elements [-13, -5, -7, -3, -6] were arranged before positive numbers [12, 11, 6, 5]. Note that there can be more than one possible output.

Input: arr[] = [11, -13, 6, -7, 5]
Output: [-13, -7, 11, 6, 5]
Explanation: All negative elements [-13, -7] were arranged before positive numbers [11, 6, 5].
'''
# def seperate_positive_and_negative(arr:list):
#     new_arr = []
#     # iterations for storing - values
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             new_arr.append(arr[i])
    
#     # iteration for storing + values
#     for i in range(len(arr)):
#         if arr[i] >= 0:
#             new_arr.append(arr[i])
            
#     return new_arr


# if __name__ == "__main__":
#     arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
#     print('Seperated Array ',seperate_positive_and_negative(arr=arr))


# def seperate_pos_neg(arr:list) -> list:
#     lo,hi = 0,len(arr) - 1
    
#     while lo < hi:
        
#         while arr[lo] < 0 and lo < hi:
#             lo += 1
#         while arr[hi] >= 0 and lo < hi:
#             hi -= 1
        
#         if lo < hi:
#             arr[lo] , arr[hi] = arr[hi],arr[lo]
#             lo += 1
#             hi -= 1
#     return arr

# if __name__ == "__main__":
#     arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
#     print("Seperated Arrray ",seperate_pos_neg(arr=arr))

'''
Q5 : Sort string of characters
Input : "dcab" 
Output : "abcd"

Input : "geeksforgeeks"
Output : "eeeefggkkorss"
'''

# def sort_string_chars(st:str) ->str :
#     return "".join(sorted(st))
# if __name__ == "__main__":
#     print("Sorted String ",sort_string_chars("geeksforgeeks"))



# Max_Char = 26

# def sort_string(string:str)->str:
#     char_count = [0] * Max_Char
#     print(string)

#     for ch in string:
#         # print(i)
#         # print(ord(ch))
#         char_count[ord(ch) - ord('a')] += 1
    
#     for i in  range(Max_Char):
#         for _ in range(char_count[i]):
#             print(chr(i + ord('a')),end='')
    
# if __name__ == "__main__":
#     string = "dcab"
#     sort_string(string=string)


'''
Q6 Sort the given matrix
Input : mat[][] = { {5, 4, 7},
                    {1, 3, 8},
                    {2, 9, 6}
                }
Output : 1 2 3
         4 5 6
         7 8 9

Input: mat[][] = { {5, 4, 7}, 
                   {1, 3, 8}
                }
Output: 1 3 4        
        5 7 8
'''
# def sort_matrix(mat:list)->list:
#     m = len(mat[0])
#     x = []
#     print("Original matrix ",mat)
    
#     # For flatening the array 
#     for arr in mat:
#         for elem in arr:
#             x.append(elem)
    
#     # using bubble sorting to sorting 1 d array
#     # for i in range(len(x)):
#         swapped = False
        
#         for j in range(0,len(x)- 1):
#             if x[j] > x[j+1]:
#                 x[j] ,x[j+1] = x[j+1] ,x[j]
#                 swapped = True
#         if swapped == False:
#             break
    
#     # using insertion sorting
#     # for i in range(1,len(x)):
#         # key = x[i]
        
#         # j = i - 1
        
#         # while j >= 0 and key < x[j]:
#         #     x[j + 1] = x[j]
#         #     j -= 1
#         # x[j + 1] = key
    
#     # using selection sorting
    
#     for i in range(len(x)):
#         min_idx = i
        
#         for j in range(i + 1,len(x)):
            
#             if x[j] < x[min_idx]:
#                 min_idx = j
                
#         x[i],x[min_idx] = x[min_idx],x[i]
    
#     print("Sorted Array ",x)
    
#     # for appending arrays into array
#     new_arr = []
#     track_index = 0
#     for i in range(len(x)):
#           new_arr.append(x[i])
#           if len(new_arr) == m:
#               mat[track_index] = new_arr
#               new_arr = []
#               track_index += 1
#     print(mat) 
         
         
# if __name__ == "__main__":
#     mat = [
#         [5,4,7],
#         [1,3,8],
#         [2,9,6]
#     ]
    
#     sort_matrix(mat=mat)


'''
Q 7 : 
'''
