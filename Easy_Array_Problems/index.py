"""
Q1 : Second largest number in an array
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34

Input: arr[] = [10, 5, 10]
Output: 5

Input: arr[] = [10, 10, 10]
Output: -1
"""

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
# def second_largest_element(arr:list,i:int = 0,largest:int=-1,second_largest:int=-1):
#     if i == len(arr):
#         return largest,second_largest
#     if arr[i] > largest:
#         second_largest = largest
#         largest = arr[i]
#     elif arr[i] < largest and arr[i] > second_largest:
#         second_largest = arr[i]
#     return second_largest_element(arr=arr,i= i+1,largest=largest,second_largest=second_largest)

# if __name__ == "__main__":
#     arr = [10, 10, 10]
#     _,second_largest = second_largest_element(arr=arr)
#     print("Second largest element ",second_largest)

"""
Q2: Third largest element in an array of distinct elements
Input: arr[] = {1, 14, 2, 16, 10, 20}
Output: 14

Input: arr[] = {19, -10, 20, 14, 2, 16, 10}
Output: 16
"""

# +++++++++++++++ Sorting approach ++++++++++++++++++
# def third_largest_element(arr:list) -> int:
#     n = len(arr)
#     arr.sort()

#     for i in range(n-3,-1,-1):
#         if arr[i] != arr[n-2]:
#             return arr[i]

#     return -1

# if __name__ == "__main__":
#     arr = [19, -10, 20, 14, 2, 16, 10]
#     print("third largest element ",third_largest_element(arr=arr))


# +++++++++++ Three pass search approach ++++++++++++++++
# def third_largest_element(arr:list):
#     largest = -1
#     second_largest = -1
#     third_largest = -1

#     # find largest element
#     for elem in arr:
#         if elem > largest:
#             largest = elem

#     for elem in arr:
#         if elem < largest and elem > second_largest:
#             second_largest = elem

#     for elem in arr:
#         if elem < largest and elem < second_largest and elem > third_largest:
#             third_largest = elem

#     return largest,second_largest,third_largest


# if __name__ == "__main__":
#     arr = [19, -10, 20, 14, 2, 16, 10]
#     _,_,third_largest = third_largest_element(arr=arr)
#     print("Third largest element ",third_largest)


# ++++++++++++++ Using three variables +++++++++++++++++
# def third_largest_element(arr: list):
#     largest = -1
#     second_largest = -1
#     third_largest = -1
#     n = len(arr)
#     for i in range(0, n):
#         if arr[i] > largest:
#             third_largest = second_largest
#             second_largest = largest
#             largest = arr[i]

#         elif arr[i] > second_largest:
#             third_largest = second_largest
#             second_largest = arr[i]
#         elif arr[i] > third_largest:
#             third_largest = arr[i]

#     return largest,second_largest,third_largest

# if __name__ == "__main__":
#     arr = [19, -10, 20, 14, 2, 16, 10]
#     _,_,third_largest = third_largest_element(arr=arr)
#     print("third largest element ",third_largest)


"""
Q3 : Reverse array 
Input: arr[] = [1, 4, 3, 2, 6, 5]  
Output:  [5, 6, 2, 3, 4, 1]

Input: arr[] = [4, 5, 1, 2]
Output: [2, 1, 5, 4]

"""


# ++++++++++++++++++++++ Naive Approach (Using temporary array ) ++++++++++++++++++++++
# def reverse_array(arr: list) -> list:
#     n = len(arr)
#     temp_arr = [] * n

#     for i in range(n-1, -1, -1):
#         temp_arr.append(arr[i])
#     return temp_arr

# if __name__ == "__main__":
#     arr = [1, 4, 3, 2, 6, 5]
#     print("Before reverse ",arr)
#     print("After reverse ",reverse_array(arr=arr))

# +++++++++++++++++++++++ Expected approach (Using two pointer) ++++++++++++++++++++++
# def reverse_array(arr:list) -> list:
#     n = len(arr)
#     left = 0
#     right = n-1
#     while left < right:
#         arr[left],arr[right] = arr[right],arr[left]
#         left += 1
#         right -=1
#     return arr

# if __name__ == "__main__":
#     arr = [1, 4, 3, 2, 6, 5]
#     print("Before reversing => ",arr)
#     print("After reversing => ",reverse_array(arr=arr))


# ++++++++++++++++++++ Expected approach By swapping ++++++++++++++++++++
# def reverse_array(arr: list) -> list:
#     n = len(arr)
#     left = 0
#     right = n - 1
#     for i in range(0, n // 2):
#         arr[left],arr[right] = arr[right],arr[left]
#         left +=1
#         right -= 1
#     return arr

# if __name__ == "__main__":
#     arr = [1, 4, 3, 2, 6, 5]
#     print("Before Reversing => ",arr)
#     print("After Reversing => ",reverse_array(arr=


"""
Q 4 : Reverse array in groups of given sizes

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
Output: [3, 2, 1, 6, 5, 4, 8, 7]

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]

Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]


"""

# ++++++++++++++ Fixed-Size group reversal ++++++++++++++++
# def group_reversal(arr:list,k:int) -> list:
#     n = len(arr)
#     i = 0
#     while i < n:
#         left = i

#         # to handle case when k is not multiple of n
#         right = min(i + k - 1,n -1)


#         # reverse the sub array
#         while left < right:
#             arr[left],arr[right] = arr[right],arr[left]

#             left += 1
#             right -= 1

#         i += k
#     return arr

# if __name__ == "__main__":
#     arr = [1, 2, 3, 4, 5, 6, 7, 8]
#     k = 3
#     print("After reversing in groups ",group_reversal(arr=arr,k=k))


"""
Q 5 : Rotate an array by d - CounterClockwise or left 
Output: {3, 4, 5, 6, 1, 2}
Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

Input: arr[] = {1, 2, 3}, d = 4
Output: {2, 3, 1}
Explanation: The array is rotated as follows:

After first left rotation, arr[] = {2, 3, 1}
After second left rotation, arr[] = {3, 1, 2}
After third left rotation, arr[] = {1, 2, 3}
After fourth left rotation, arr[] = {2, 3, 1}
"""


# +++++++++++++++ Naive approach (rotate one by one) +++++++++++++++++++
# def rotate_array_by_d(arr:list,d:int) -> list:
#     n  = len(arr)
    
#     for i in range(d):
        
#         first = arr[0]
#         for j in range(0,n - 1):
#             arr[j] = arr[j + 1]
#         arr[n - 1] = first
#     return arr

# if __name__ == "__main__":
#     arr = [1,2,3,4,5]
#     d = 2
#     print("After rotation to the left ",rotate_array_by_d(arr=arr,d=d))


# ++++++++++++++++ Better approach (Using temporary array ) ++++++++++++++++++++
# def rotate_array(arr:list,d:int) -> list:
#     n = len(arr)
#     temp_array = [0] * n
    
#     d %= n
    
#     # Copy last n - d elements to the fron of temp_array 
#     for i in range(n - d):
#         temp_array[i] = arr[d + i]
    
    
#     # copy the first d elements to the back of the temp_array
    
#     for i in range(d):
#         temp_array[n - d + i] = arr[i]
    
    
#     # copying the elements of temp_arr in arr to get the final rotated array
#     for i in range(n):
#         arr[i] = temp_array[i]


# if __name__ == "__main__":
#     arr = [1,2,3,4,5]
#     d = 2
#     rotate_array(arr=arr,d=d)
#     for elem in arr:
#         print(elem,end=' ')
#     # print("Array after rotation ",rotate_array(arr=arr,d=d)) 
    