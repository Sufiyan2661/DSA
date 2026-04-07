"""
Q1 : Next Permuation
nput: arr[] = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next lexicographically greater arrangement of the elements in the array arr[] is [2, 4, 5, 0, 1, 7].

Input: arr[] = [3, 2, 1]
Output: [1, 2, 3]
Explanation: This is the last permutation, so we return the lowest possible permutation (ascending order).

Input: arr[] = [1, 3, 5, 4, 2]
Output: [1, 4, 2, 3, 5]
Explanation: The next lexicographically greater arrangement of the elements in the array arr[] is [1, 4, 2, 3, 5].
"""

# +++++++++++++++++++++++++++++++++++++ Better approach using traversing from right to left
# def next_permuation(arr:list[int]) -> list[int]:
#     n = len(arr)


#     # step 1 find the breaking point traversing from right to left
#     i = n - 2
#     while i >= 0 and arr[i] >= arr[i + 1]:
#         i -= 1


#     # step 2
#     if i >= 0:
#         j = n - 1
#         while arr[j] <= arr[i]:
#             j  -= 1
#         arr[i],arr[j] = arr[j],arr[i]


#     left = i + 1
#     right = n - 1

#     while left < right:
#         arr[left],arr[right] = arr[right],arr[left]

#         left += 1
#         right -= 1


#     return arr


# if __name__ == "__main__":
#     arr = [1, 3, 5, 4, 2]
#     print("New Array ",next_permuation(arr=arr))


"""
Q2: Majority element
Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
Output: 1
Explanation: Element 1 appears 4 times. Since ⌊7/2⌋ = 3, and 4 > 3, it is the majority element.

Input: arr[] = [7]
Output: 7
Explanation: Element 7 appears once. Since ⌊1/2⌋ = 0, and 1 > 0, it is the majority element.

Input: arr[] = [2, 13]
Output: -1
Explanation: No element appears more than ⌊2/2⌋ = 1 time, so there is no majority element.

"""

# +++++++ Naive approach using two nested loops
# def majority_element(arr:list) -> int:
#     n = len(arr)

#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i] == arr[j]:
#                 count += 1

#         if count > n // 2:
#             return arr[i]
#     return -1


# ++++++++++++++++=== Better approach using sorting
# def majority_element(arr:list) -> int:
#     n = len(arr)
#     arr.sort()

#     candidate = arr[n//2]
#     print("Candidate ",candidate)

#     count = 0
#     for i in range(n):
#         if arr[i] == candidate:
#             count += 1
#     if count > n // 2:
#         return candidate
#     else:
#         return -1


# Better approach using hasing
# from collections import defaultdict
# def majority_element(arr:list) -> int:

#     n = len(arr)

#     hash_map = defaultdict(int)

#     for num in arr:
#         hash_map[num] += 1

#         if hash_map[num] > n /2:
#             return num
#     return -1


# def majority_element(arr:list) -> int:
#     pass


# if __name__ == "__main__":
#     arr =  [1, 2, 2, 2, 3, 5, 2]
#     elem = majority_element(arr=arr)
#     print("Majority ",elem)


"""
Q3 Majority Element II - Elements occurring more than ⌊n/3⌋ times
Input: arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
Output: [1, 2]
Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).

Input: arr[] = [-5, 3, -5]
Output: [-5]
Explanation: The frequency of -5 is 2, which is more than floor n/3 (3/3 = 1).

Input: arr[] = [3, 2, 2, 4, 1, 4]
Output: [ ]
Explanation: There is no majority element.
"""
# ++++++++++++++ Naive approach using nested loops

# def majority_elements(arr:list) ->list:
#     n = len(arr)
#     new_arr = []
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[i] == arr[j]:
#                 count += 1
#         if count > n // 3:

#             if len(new_arr) == 0 or arr[i] != new_arr[0]:
#                 new_arr.append(arr[i])


#         if len(new_arr) == 2:
#             print("in this condition ")

#             if new_arr[0] > new_arr[1]:
#                 new_arr[0],new_arr[1] = new_arr[1],new_arr[0]
#             break


#     return new_arr

# ++++++++++++++++++++++++++++++++++ Better Approach Using Hash Map
# def majority_elements(arr:list) -> list:
#     n = len(arr)
#     freq = {}
#     new_arr = []
#     for ele in arr:
#         freq[ele] = freq.get(ele,0)  + 1


#     print(freq)
#     for key,value in freq.items():
#         if value > n // 3:
#             new_arr.append(key)

#         if len(new_arr) == 2 and new_arr[0] > new_arr[1]:
#             new_arr[0],new_arr[1] = new_arr[1],new_arr[0]
#             return new_arr


#     return new_arr


# if __name__ == "__main__":
#     arr = [2, 2, 3, 1, 3, 2, 1, 1]
#     print("Array ",majority_elements(arr=arr))


"""
Q4 Minimize the maximum difference between the heights
Input: k = 2, arr[] = [1, 5, 8, 10]
Output: 5
Explanation:  The array can be modified as [1+k, 5-k, 8-k, 10-k]= [3, 3, 6, 8]. The difference between the largest and the smallest is 8 - 3 = 5.

Input: k = 3, arr[] = [3, 9, 12, 16, 20]
Output: 11
Explanation: The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] = [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 17 - 6 = 11.
"""
# def get_min_diff(arr:list,k:int) -> int:
#     n = len(arr)
#     arr.sort()

#     ans = arr[n - 1] - arr[0]
#     smallest = arr[0] + k
#     lg = arr[n - 1] - k
#     for i in range(1,n):
#         if arr[i] - k < 0:
#             continue
#         min_h = min(arr[0] + k,arr[i] - k)
#         max_h = max(arr[n - 1] - k,arr[i - 1] + k)
#         ans = min(ans,max_h - min_h)
#     return ans


# if __name__ == "__main__":
#     arr = [3, 9, 12, 16, 20]
#     k = 3
#     print("Minimum difference ",get_min_diff(arr=arr,k=k))


"""
Q5 :Maximum Subarray Sum - Kadane's Algorithm
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray [-2] has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray [5, 4, 1, 7, 8] has the largest sum 25.
"""
# [Naive Approach] By iterating over all subarrays - O(n^2) Time and O(1) Space
# def sum_of_max_sub_array(arr:list)->int:
#     n = len(arr)

#     res = arr[0]

#     for i in range(n):

#         current_sum = 0

#         for j in range(i,n):

#             current_sum += arr[j]

#             res = max(res,current_sum)
#     return res

# if __name__ == "__main__":
#     arr = [2, 3, -8, 7, -1, 2, 3]
#     print("Result ",sum_of_max_sub_array(arr=arr))


# [Expected Approach] Using Kadane's Algorithm - O(n) Time and O(1) Space


# def sum_of_max_sub_array(arr:list)->int:
#     n = len(arr)

#     result = arr[0]

#     max_ending = arr[0]

#     for i in range(1,n):

#         max_ending = max(max_ending + arr[i],arr[i])


#         result = max(result,max_ending)
#     return result

# if __name__ == "__main__":
#     arr = [2, 3, -8, 7, -1, 2, 3]
#     print("Result ",sum_of_max_sub_array(arr=arr))

"""
Q6 : Maximum product of subarray
Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.

Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 
"""

# [Naive Approach] Using Two Nested Loops – O(n^2) Time and O(1) Space
# def max_product(arr:list)->int:
#     n = len(arr)

#     result = arr[0]
#     for i in range(n):

#         current_product = 1

#         for j in range(i,n):

#             current_product *= arr[j]


#             result = max(result,current_product)

#     return result


# if __name__ == "__main__":
#     arr = [-2, 6, -3, -10, 0, 2]
#     print("Result ",max_product(arr=arr))


# [Expected Approach - 1] Track of Min and Max - O(n) Time and O(1) Space
# def max_product(arr:list)->int:
#     n = len(arr)

#     curr_max = arr[0]

#     curr_min = arr[0]


#     max_prod = arr[0]
#     for i in range(1,n):


#         # temporary variable to store the maximum product ending at the current index
#         temp = max(arr[i],arr[i] * curr_max, arr[i] * curr_min)


#         # update the minimum product ending at the current index

#         curr_min = min(arr[i],arr[i] * curr_max,arr[i] * curr_min)

#         curr_max = temp

#         # update the overall maximum product
#         max_prod = max(max_prod,curr_max)


#     return max_prod

# if __name__ == "__main__":
#     arr = [-2, 6, -3, -10, 0, 2]
#     print("Result ",max_product(arr=arr))


# [Expected Approach - 2] By Traversing in Both Directions - O(n) Time and O(1) Space
# def max_prod(arr: list) -> int:
#     n = len(arr)

#     max_prod = float("-inf")

#     left_to_right = 1

#     right_to_left = 1
#     breakpoint()

#     for i in range(n):
#         breakpoint()
#         if left_to_right == 0:
#             left_to_right = 1
#         if right_to_left == 0:
#             right_to_left = 1
#         breakpoint()
#         # calculate product from index left to right
#         left_to_right *= arr[i]

#         # calculate index from right to left
#         j = n - i - 1
#         right_to_left *= arr[j]
#         breakpoint()
#         max_prod = max(left_to_right, right_to_left, max_prod)
#         breakpoint()
#     breakpoint()

#     return max_prod


# if __name__ == "__main__":
#     arr = [-2, 6, -3, -10, 0, 2]
#     print("Result ", max_prod(arr=arr))



'''
Q7 : Product of Array Except Self
Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: 
For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.

Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: 
For i = 0, res[i] = 0.
For i = 1, res[i] = 12.
'''

# Naive approach using nested loops


# def product_array(arr:list[int])->list[int]:
    
#     n = len(arr)
    
#     result = [1] * n
    
    
#     for i in range(n):
        
#         for j in range(n):
#             if arr[j] != arr[i]:
#                 result[i] *= arr[j]
    
    
#     print("Result ",result)

'''
tc  = O(n*2)
sc = O(n)
'''
    

# if __name__ == "__main__":
#     arr = [10, 3, 5, 6, 2]
    
#     product_array(arr=arr)


# def array_product(arr:list[int])->list[int]:
#     n = len(arr)
#     pref_proudct = [1] * n  
#     suff_product = [1] * n
#     res = [0] * n

    
#     # calulating prefix product
#     for i in range(1,n):
#         pref_proudct[i] = arr[i - 1] * pref_proudct[i - 1]
    
#     print("prefix product ",pref_proudct)
    
#     # calculating postfix product 
#     for i in range(n - 2,-1,-1):
#         suff_product[i] = arr[i + 1] * suff_product[i + 1]
        
#     for i in range(n):
#         res[i] = suff_product[i] * pref_proudct[i]


#     return res
    
'''
tc = O(n)
sc = O(n)

'''

# if __name__ == "__main__":
#     arr = [10, 3, 5, 6, 2] 
    
#     result = array_product(arr=arr)
#     print("Result ",result)



# Efficient approach using product array 

# def prod_array_exc_self(arr:list[int])->list[int]:
#     zeros = 0
#     idx = -1
#     prod = 1
    
#     for i in range(len(arr)):
        
#         if arr[i] == 0:
#             zeros += 1
#             idx = i
#         else:
#             prod *= arr[i]
    
    
#     result  = [0] * len(arr)
    
#     print("Zeors ",zeros)
#     print("Product ",prod)
#     if zeros == 0:
        
#         for i in range(len(arr)):
#             result[i] = prod // arr[i]
            
#     elif zeros == 1:
#         result[idx] = prod
    
    
#     return result


# if __name__ == "__main__":
#     arr = [10, 3, 5, 6, 2]
#     print("Result ",prod_array_exc_self(arr=arr))



'''
Q8 : Subarrays having product less than K
Input : arr[] = [1, 2, 3, 4] 
            K = 10
Output : 7
The subarrays are {1}, {2}, {3}, {4}, {1, 2}, {1, 2, 3} and {2, 3}

Input  : arr[] = [1, 9, 2, 8, 6, 4, 3] 
             K = 100
Output : 16

Input  : arr[] = [10, 5, 2, 6]  
             K = 100
Output : 8
'''
# def count_array(arr:list[int],k:int)->int:
#     count = 0
    
#     for i in range(len(arr)):
        
#         # counter for single element
#         if arr[i] < k:
#             count += 1
#         mul  = arr[i]
#         for j in range(i + 1,len(arr)):
            
            
#             # multiply subarray
#             mul = mul * arr[j]
            
#             if mul < k:
#                 count += 1
#             else:
#                 break
#     return count
# '''
# tc = O(n * 2)
# sc = O(1)
# '''

# if __name__ == "__main__":
#     arr = [1, 2, 3, 4]
#     print("Result ",count_array(arr=arr,k=10))



# def count_array(arr:list[int],k:int)->int:
#     n = len(arr)
    
#     p =1
#     res = 0
#     start = 0
#     end = 0
    
#     while end < 0:
        
        
#         # Move right bound by one step. Update product 
#         p *= arr[end]
        
        
#         # Move left bound so gaurantee that p is  again less than k
#         while start < end  and p >= k:
#             p = int(p // arr[start])
#             start += 1
            
        
#         # if p < k , update count : this also works when start == end, meaning only single forms the window.
#         if p < k:
#             l = end - start + 1
#             res += 1

#         end += 1
    
#     return res
        

# if __name__ == "__main__":
#     arr = [1, 2, 3, 4]
#     print("Result ",count_array(arr=arr,k=10))


# result = sum([1,8,6,2,5,4,8,3,7])
# print("Result ",result)