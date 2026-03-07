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

"""
operations for tc:
    n = len(arr) takes constan times O(1)
    arr.sort() the worst case can take upto O(n log n)
    for i in range(n - 2,-1,-1) iterating lenearly in reverse order so it can take n number of iterations to perform constant taks O(n)
    tc = O(1) + O(n log n) + O(n) = O(n log n)
operations for sc:
    n = len(arr) takes constant space O(1)
    arr.sort() can takes upto n number of space in the worst case O(n)
    sc = O(1) + O(n) = O(n)
"""


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


"""
tc = O(n)
sc = O(1)
"""
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

"""
tc = O(n)
sc = O(1)
"""

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
"""
tc = O(n)
sc = O(n) the variables stays in the call untill it reaches base 
"""

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
"""
tc = O(n)
sc = O(1)
"""

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

"""
tc = O(n)
sc = O(1)
"""

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

"""
tc = O(n)
sc = O(1)

"""

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
"""
operations for tc:
    n = len(arr) takes constant time because len initialize when data structure is used so O(1)
    temp_arr = [0] * n takes constant time O(1)
    for i in range(n-1,-1,-1) iterate linearly so if array has n number of elements it can take n number of time to iterate O(n)
    temp_arr.append(arr[i]) takes constant time O(1)
    tc = O(1) + O(1) + O(n) + O(1) = O(n)
    tc = O(n)
operations for sc:
    n = len(arr) takes constant space O(1)
    temp_arr = [0] * n here it takes n number of space because size grows as the input grows so it takes O(n) space
    i for iterating takes constant space in each iteration O(1)
    sc = O(1) + O(n) O(1) = O(n)
    sc = O(n)
"""

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
"""
operations for tc:
    n = len(arr) takes constant time O(1)
    left = 0 takes constatn time O(1)
    right = n - 1 takes constant time O(1)
    while left < right it take iterate n times if array has n elements right  = n -1 so it iterate upto O(n - 1) so tc for this operation is O(n)
    arr[left],arr[right] = arr[right],arr[left] takes constant time 
    left += 1 takes constant time
    right -= 1 takes constant time
operations for sc :
    n = len(arr) takes constant time O(1)
    left = 0 takes constatn time O(1)
    right = n - 1 takes constant time O(1)
    sc = O(1) + O(1) + O(1) = O(1)

"""

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

"""
Q5 Maximum product of triplet (subsequence of size 3) in array
Input:  arr[ ] = [10, 3, 5, 6, 20]
Output: 1200
Explanation: Multiplication of 10, 6 and 20

Input:  arr[ ] =  [-10, -3, -5, -6, -20]
Output: -90

Input: arr[ ] =  [1, -4, 3, -6, 7, 0]
Output: 168
"""
# +++++++++++++++++++++ Naive approach (nested iteration) +++++++++++++++++++++++++++++
# def max_prod_of_triplet(arr:list) -> None:
#     n = len(arr)

#     max_product = -10**9
#     for i  in range(n-2):
#         for j in range(i+1,n-1):
#             for k in range(j+1,n):
#                 max_product = max(max_product,arr[i] * arr[j] * arr[k])
#     return max_product
"""
operations for tc:
    n = len(arr) takes constant time because it already created when using any data structure O(1)
    for i  in range(n-2) takes n - 2 times to iterate so it is O(n)
    for j in range(i+1,n-1) it statrt i + 1 and iterate till n - 1 for each iteration for i it iterate till n O(n)
    for k in range(j+1,n) it also depends of iteration of k so if array has n elements it can also go upto n elements O(n)
    max_product = max(max_product,arr[i] * arr[j] * arr[k]) its takes a constatn operation O(1)
    tc = O(1) + O(n) * O(n) * O(n) * O(n) * O(1) don`t count constants when calculating tc
    tc = O(n) * O(n) * O(n) * O(n)
    tc = O(n3)
operations of sc:
    max_product this is the only variables beside input and it is constant and doesn`t grow according to the input so the space complexity of this code is O(1)
    sc = O(1)
"""
# if __name__ == "__main__":
#     arr = [10, 3, 5, 6, 20]
#     print("triplet ",max_prod_of_triplet(arr=arr))


# +++++++++++++++ Better approach (By using sorting) ++++++++++++++++++++
# def max_prod_of_triplet(arr: list) -> None:
#     n = len(arr)
#     arr.sort()
#     # print("arr of 0 ",arr[0],"array of 1",arr[1],"array of n - 1",arr[n-1],"array of n - 2",arr[n -2],"array of n - 3",arr[n - 3])
#     return max(arr[0] * arr[1] * arr[n - 1], arr[n - 1] * arr[n - 2] * arr[n - 3])


"""
operations of tc:
    n = len(arr) takes constant time
    arr.sort() .sort() can takes upto O(n log n) in worst case so O(n log n)
    return max(arr[0] * arr[1] * arr[n - 1], arr[n - 1] * arr[n - 2] * arr[n - 3]) takes constant time O(1)
    tc = O(n log n)
operations for sc:
    n = len(arr) taking variable n to store the length of array it takes constant space O(1)
    sc = O(1)
"""
# if __name__ == "__main__":
#     arr = [10, 3, 5, 6, 20]
#     print("max of triplet ",max_prod_of_triplet(arr=arr))


# ++++++++++++ Expected approach (By using  greedy approach ) ++++++++++
# def max_prod_of_triplet(arr: list):
#     largest = 0
#     second_largest = 0
#     third_largest = 0
#     for elem in arr:
#         if elem > largest:
#             third_largest = second_largest
#             second_largest = largest
#             largest = elem

#         elif elem > second_largest and elem < largest:
#             third_largest = second_largest
#             second_largest = elem

#         elif elem > third_largest and elem < largest and elem < second_largest:
#             third_largest = elem

#     return largest * second_largest * third_largest
"""
operations for tc:
    initializing three variables for storing largest,second_largest,and  third_largest takes constant time O(1)
    for elem in arr here i perform iteration for each element if the array has n elements then iteration takes n time to perform each constant operations inside the loop O(n)
    tc = O(n)
operations for sc:
    initializing three variables for storing largest,second_largest,and  third_largest takes constant space O(1)
    sc = O(1)
"""
# if __name__ == "__main__":
#     arr = [10, 3, 5, 6, 20]
#     print("maximum product of triplet ", max_prod_of_triplet(arr=arr))


"""
Q6 : Maximum consecutive one’s (or zeros) in a binary array
Input: arr[] = [0, 1, 0, 1, 1, 1, 1]
Output: 4
Explanation: The maximum number of consecutive 1’s in the array is 4 from index 3-6.

Input: arr[] = [0, 0, 1, 0, 1, 0]
Output: 2
Explanation: The maximum number of consecutive 0’s in the array is 2 from index 0-1.

Input: arr[] = [0, 0, 0, 0]
Output: 4
Explanation: The maximum number of consecutive 0’s in the array is 4.
"""

# ++++++++++++++++++++ Using simple traversal ++++++++++++=
# def most_consecutive_bits(arr:list):
#     max_streak_of = 0
#     count = 0
#     n = len(arr)
#     for i in range(n -1):
#         if arr[i] == arr[n - 1]:
#             count+=1
#         else:
#             max_streak_of =  max(max_streak_of,count)
#             count = 1
#     print("max streak of ",max_streak_of)
#     print("max count ",count)
#     return max(max_streak_of,count)

"""
operations for tc:
    initializing three variables max_streak_of , count , n takes constant time O(1)
    for i in range(n-1) iterating array and performing constant operations on each iteration and iteration can happen in worst case takes O(n)
    tc = O(1) + O(n)
    tc = O(n)
operations for sc:
    initializing only three variables takes constant space O(1)
    sc = O(1)
"""


# if __name__ == "__main__":
#     arr = [0, 1, 0, 1, 1, 1, 1]
#     print(most_consecutive_bits(arr=arr))

"""
Q7: Move all Zeros to End of Array
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
"""
# +++++++++++++++ Naive approach (Using temporary array )
# def move_zero_to_end(arr:list)->list:
#     n = len(arr)
#     temp = [0] * n
#     # to track the index
#     j = 0
#     for i in range(n):
#         if arr[i] != 0:
#             temp[j] = arr[i]
#             j += 1
#     while j < n:
#         arr[j] = 0
#         j +=1

#     for i in range(n):
#         arr[i] = temp[i]
#     return arr
"""
tc = O(n)
sc = O(n)
"""
# if __name__ == "__main__":
#     arr = [1, 2, 0, 4, 3, 0, 5, 0]
#     print("list zeros in the end ",move_zero_to_end(arr=arr))

# +++++++++++++ Better approach (Two traversal) +++++++++++
# def move_zero_to_end(arr:list) -> list:
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         if arr[i] != 0:
#             arr[count] = arr[i]
#             count +=1
#     while count < n:
#         arr[count] = 0
#         count +=1
#     return arr
"""
operations for tc:
    initializing three variables takes constant time O(1)
    for i in range(n) iterating till n number of elements take n times to perform constant operations in each iteration O(n)
    while count < n then iterating till n if the array has n number of zeros it can iterate upto n so in worst case it can take n times to perform constant operation on each iteration O(n)
    tc = O(1) + O(n) + O(n) = O(2n) here we ignore constant 
    tc = O(n)
operations for sc:
    initializing three variables takes constant space O(1)
    sc = O(1)
    
"""
# if __name__ == "__main__":
#     arr = [1, 2, 0, 4, 3, 0, 5, 0]
#     print("Move zero`s to end ",move_zero_to_end(arr=arr))

# ++++++++++++++++ Expected approach (one traversal) +++++++++++++
# def move_zeor_to_end(arr:list) -> list:
#     count = 0
#     n = len(arr)
#     for i in range(n):

#         if arr[i] != 0:
#             arr[i],arr[count] = arr[count],arr[i]
#             count +=1
#     return arr
"""
TC = O(n)
SC = O(1)
"""

# if __name__ == "__main__":
#     arr = [1, 2, 0, 4, 3, 0, 5, 0]
#     print("Moved zeor to end ",move_zeor_to_end(arr=arr))

# ++++++++++++++ one traversal approach (with creating another arr of the size n of input arr) ++++++++++++++
# def move_zero_to_end(arr:list) ->list:
#     n = len(arr)
#     j = 0
#     new_arr = [0] * n
#     for i in range(n):
#         if arr[i] != 0:
#             new_arr[j] = arr[i]
#             j += 1
#     return new_arr

"""
TC = O(n)
SC = O(1)
"""
# if __name__ == "__main__":
#     arr = [1, 2, 0, 4, 3, 0, 5, 0]
#     print("Moved zeor to end ",move_zero_to_end(arr=arr))


"""
Q8: Sort an array in wave form
Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

Input: arr[] = [2, 4, 7, 8, 9, 10]
Output: [4, 2, 8, 7, 10, 9]
Explanation: Array elements after sorting it in the waveform are 4, 2, 8, 7, 10, 9.
"""


# def sort_in_wave(arr: list) -> None:
#     n = len(arr)
#     for i in range(0,n-1,2):
#         arr[i],arr[i+1] = arr[i+1],arr[i]
"""
TC = O(n)
SC = O(1)
"""
# if __name__ == "__main__":
#     arr = [1,2,3,4,5]
#     sort_in_wave(arr=arr)
#     print("array after sorted in wave ",arr)


"""
Q8 adding one to number represented as array of digits
Input : [1, 2, 4]
Output : 125
Explanation: 124 + 1 = 125 

Input : [9, 9, 9]
Output: 1000
Explanation: 999 + 1 = 1000 
"""
# def add_one_number(arr:list)->int:
#     carry = 1
#     for i in range(len(arr)-1,-1,-1):
#         sum_ = arr[i] + carry
#         arr[i] = sum_ % 10
#         carry = sum_ // 10
#     if carry:
#         arr.insert(0,carry)
#     return arr
# if __name__ == "__main__":
#     arr = [1, 2, 4]
#     print("Add one ",add_one_number(arr=arr))
"""
Q9 Median of two sorted array
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

# ++++++++++++++ My Approach ++++++++++++++++

# def array_median(arr1:list[int],arr2:list[int]) -> float:
#     new_arr = arr1 + arr2
#     new_arr.sort()
#     print("array after sorting ",new_arr)
#     n = len(new_arr)
#     print("len ",n)
#     if n % 2 == 0:
#         mid1 = (n // 2) -1
#         print("mid 1 ",mid1)
#         mid2 = n // 2
#         print("mid 2 ",mid2)
#         return (new_arr[mid1] + new_arr[mid2]) / 2
#     else:
#         mid = n // 2
#         return float(new_arr[mid])
# if __name__ == "__main__":
#     nums1 = [1,3,7,78,34,56]
#     nums2 = [2,4,3,5,3,2]
#     print("Media of two array ",array_median(nums1,nums2))


"""
Q10: Stock Buy and Sell - Max one Transaction Allowed
Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: Buy for price 1 and sell for price 9. 

Input: prices[] = [7, 6, 4, 3, 1]
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = [1, 3, 6, 9, 11]
Output: 10
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]
"""


# +++++++++++++++++++++ Naive approach (By exploring all possible pairs ) +++++++++++++++++++++++=
# def max_profit(prices:list)->int:
#     n = len(prices)
#     res = 0

#     for i in range(n - 1):
#         for j in range(i + 1,n):
#             res = max(res,prices[j] - prices[i])
#     return res
"""
tc = 0(n*2)
sc = 0(1)
"""
# if __name__ == "__main__":
#     arr = [1, 3, 6, 9, 11]
#     print("Max profit ",max_profit(prices=arr))


# ++++++++++++++++++++++++++ Expected approach (One traversal approach ) ++++++++++++++++++++++++++++++
# def max_profit(prices: list) -> int:
#     min_so_far = prices[0]
#     res = 0

#     for i in range(1, len(prices)):

#         min_so_far = min(min_so_far, prices[i])

#         res = max(res, prices[i] - min_so_far)
#     return res

# if __name__ == "__main__":
#     arr = [1, 3, 6, 9, 11]
#     print("max profit ", max_profit(prices=arr))


"""
Q 11 Stock Buy and Sell - Multiple Transaction Allowed
Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865

Input: prices[] = [4, 2]
Output: 0
"""

# +++++++++++++ Naive approach (By Trying all possibility) ++++++++++++
# def max_profit(price,start,end):
#     res = 0
#     for i in range(start,end):
#         for j in range(i +1,end + 1):


# # Better Approach iterative O(n) and O(1)
# def max_profit(prices):


#     profit = 0

#     for i  in range(1,len(prices)):
#         if prices[i] > prices[i -1]:
#             profit += prices[i] - prices[i - 1]
#     return profit


# if __name__ == "__main__":
#     prices = [100, 180, 260, 310, 40, 535, 695]
#     print("Max profit ",max_profit(prices=prices))


"""
Q12 Remove duplicates from Sorted Array

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: All the elements are 2, So only keep one instance of 2.

Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
Output: [1, 2, 3, 4, 5]

Input: arr[] = [1, 2, 3]
Output: [1, 2, 3]
Explanation : No change as all elements are distinct.
"""
# +++++++++++++++++= Using Set
# def remove_duplicates(arr:list) -> int:
#     seen = set()
#     idx = 0
#     for i in range(len(arr)):
#         if not arr[i] in seen:
#             seen.add(arr[i])
#             arr[idx] = arr[i]
#             idx += 1
#     return idx

"""
operations for tc:
    initializing two variables (seen:set) and (idx:int) takes constant time O(1)
    iteranting each element takes O(n) and inside each iteration performing consant operation
    tc = O(1) + O(n)
    tc = O(n)
operations sc:
    intiailizing variables seen of type set which can be store n number of elements so its sc will be O(n)
    initializing idx to track the index of that value so it is O(1)
    sc = O(n) + O(1)
    sc = O(n)
"""

# if __name__ == "__main__":
#     arr = [1, 2, 3]
#     new_size = remove_duplicates(arr=arr)
#     for i in range(new_size):
#         print(arr[i],end=" ")


# def remove_duplicate(arr:list)->int:
#     n = len(arr)
#     if n <= 1:
#         return n
#     idx = 1
#     for i in range(1,n):
#         if arr[i] != arr[i - 1]:
#             arr[idx] = arr[i]
#             idx +=1
#     return idx
"""
operations for tc:
    intializing two variables of type int one to store the lenght of the array and other to track index of the elements both takes constant time O(1)
    iterating each element takes n times if the array has n number of elements  and inside each iteration we are performing contant operations so here we ignore constant and the time complexity will be O(n)
    tc = O(1) + O(n)
    tc = O(n)
operatons for sc:
    initializing variable n it takes constant space O(1)
    initializing variable idx to track the index also takes constant space O(1)
    and using variable i for iteration of each index also takes constant space 
    sc = O(1)
"""

# if __name__ == "__main__":
#     arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
#     new_size = remove_duplicate(arr=arr)
#     for i in range(new_size):
#         print(arr[i],end=" ")


"""
Q13: Rearrange Array Elements by Sign

Input:  arr[] = [1, 2, 3, -4, -1, 4]
Output: arr[] = [1, -4, 2, -1, 3, 4]

Input:  arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
Output: arr[] = [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
"""


# def right_rotate(arr: list, start: int, end: int) -> None:
#     temp = arr[end]
#     for i in range(end, start, -1):
#         arr[i] = arr[i - 1]
#     arr[start] = temp


# def rearange_array(arr: list) -> None:
#     n = len(arr)
#     for i in range(n):
#         # Check if current positive element is out of place
#         if arr[i] >= 0 and i % 2 == 1:
#             # Find the next negative element and rotate the subarray
#             for j in range(i + 1, n):
#                 if arr[j] < 0:
#                     right_rotate(arr=arr, start=i, end=j)
#                     break
#         elif arr[i] < 0 and i % 2 == 0:
#             # find the next positive element and rotate the sub array
#             for j in range(i + 1, n):
#                 if arr[j] >= 0:
#                     right_rotate(arr, i, j)
#                     break





# if __name__ == "__main__":
#     arr = [1, 2, 3, -4, -1, 4]
#     rearange_array(arr=arr)
#     print(" ".join(map(str, arr)))


'''
Q14 : Leaders in an array
Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right 
i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
'''

# +++++++++++++++++++ Naive approach using nested loops ++++++++++++++++++++++++++
# def leaders(arr:list) -> list:
#     n = len(arr)
#     result = []
#     for i in range(n):
#         for j in range(i + 1,n):
#             if arr[i] < arr[j]:
#                 break
#         else:
#             result.append(arr[i])
#     return result

# if __name__ == "__main__":
#     arr = [16, 17, 4, 3, 5, 2]
#     new_arr = leaders(arr=arr)
#     print("New Array ",new_arr)


# +++++++++++++++++++++ Using expected approach ++++++++++++++++++
# def leaders(arr:list) -> list:
#     n = len(arr)
#     result = []
#     max_right = arr[-1]
    
#     result.append(max_right)
#     for i in range(n-2,0,-1):
#         if arr[i] >= max_right:
#             max_right = arr[i]
#             result.append(max_right)
#     result.reverse()
#     return result
        
# if __name__ == "__main__":
#     arr = [16, 17, 4, 3, 5, 2]
#     new_array = leaders(arr=arr)
#     print("New Array ",new_array)
    
    
    

'''
Q15: Missing ranges of numbers
Input: arr[] = [14, 15, 20, 30, 31, 45], lower = 10, upper = 50
Output: [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]
Explanation: These ranges represent all missing numbers between 10 and 50 not present in the array
Input: arr[] = [-48, -10, -6, -4, 0, 4, 17], lower = -54, upper = 17
Output: [[-54, -49], [-47, -11], [-9, -7], [-5, -5], [-3, -1], [1, 3], [5,16]]
Explanation: These ranges represent all missing numbers between -54 and 17 not present in the array.
'''

# def missing_ranges(arr:list,lower:int,upper):
#     n = len(arr)
#     res = []
    
    
#     # if first element is greater than lower
#     if arr[0] > lower:
#         res.append([lower,arr[0] - 1])
    
#     for i in range(n - 1):
#         if arr[i + 1] - arr[i] > 1:
#             res.append([arr[i] + 1,arr[i + 1] - 1])
    
    
#     if upper > arr[-1]:
#         res.append([arr[-1] + 1, upper])

#     return res

'''

'''

# if __name__ == "__main__":
#     lower = 10
#     upper = 50
#     arr = [14, 15, 20, 30, 31, 45]
#     res =  missing_ranges(arr=arr,lower=lower,upper=upper)
#     print("Result ",res)
    
#     for v in res:
#         print(v[0],v[1])


'''
Q16: Sum of all subarrays
Input: arr[] = [1, 4, 5, 3, 2]
Output: 116
Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

Input: arr[] = [1, 2, 3, 4]
Output: 50
Explanation: Sum of all possible subarrays of the array [1, 2, 3, 4] is 50.
'''

# ++++++++++ Naive Approach using nested loops +++++++++++++++++++++
# def sum_of_subarrays(arr:list) -> int:
#     n = len(arr)
#     result = 0
    
#     for i in range(n):
#         temp = 0
        
#         for j in range(i,n):
#             temp  += arr[j]
#             result += temp
    
#     return result


# if __name__ == "__main__":
#     arr = [1, 4, 5, 3, 2]
#     result = sum_of_subarrays(arr=arr)
#     print("Sub of sum arrays ",result)



# +++++++++++ Expected Approach Element Contribution method ++++++++++++++++++
# def sum_of_subarrays(arr:list) ->int:
#     answer = 0
#     n = len(arr)
    
#     for i in range(n):
#         answer += arr[i] * (i+1) * (n-i)
    
    
#     return answer


# if __name__ == "__main__":
#     arr = [1, 4, 5, 3, 2]
#     result = sum_of_subarrays(arr=arr)
#     print("Result ",result)
    
            