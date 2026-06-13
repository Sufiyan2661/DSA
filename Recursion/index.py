"""
Q 1 Print number from 1 to n
"""

# def print_number(n, i = 1):
#     if i > n:
#         return
#     print(i)
#     print_number(n,i+1)

# print_number(5)


"""
Q2 : Print numbers from N to 1
"""
# def n_to_one(n):
#     if n == 0:
#         return
#     print(n)
#     n_to_one(n -1)


# n_to_one(5)


"""
Q3 : . Sum of first N natural numbers
"""

# def sum_of_n(n):
#     if n == 1:
#         return 1
#     return n + sum_of_n(n - 1)

# print("ans ",sum_of_n(5))


"""
Q 4: Factorial of a number
"""
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# print("Ans ",fact(4))

"""
Q 5: Power function
"""

# def power(n,pow):
#     if pow == 1:
#         return n
#     return n * power(n,pow - 1)

# print("ans ",power(2,5))

"""
Q 6: Count digits in a number
"""
# def count_digit(digit,count = 0):
#     if digit == 0 and count == 0:
#         return 1
#     if digit == 0:
#         return count
#     return count_digit(digit// 10,count + 1)


# print("ans ",count_digit(0))


"""
Q 7:  Sum of digits
"""
# def sum_of_digits(digit,sm = 0):
#     if digit == 0 and sm == 0:
#         return -1
#     if digit == 0:
#         return sm
#     sm += digit % 10
#     return sum_of_digits(digit// 10,sm)

# print("ans ",sum_of_digits(1))


"""
Q 8: REverse digit
"""
# def rev_digit(digit,rev = 0):
#     if digit == 0:
#         return rev
#     rev = (rev * 10) + digit % 10
#     return rev_digit(digit // 10,rev)


# print('Ans ',rev_digit(123))

"""
Q 9 : Check palindrome number/string
"""
# def palindrome(digit,rev = 0,temp = 0):
#     if digit == 0:
#         return rev == temp
#     if rev == 0:
#         temp = digit
#     rev = (rev * 10) + digit % 10
#     return palindrome(digit// 10,rev,temp)

# def palindrome(digit,rev = 0):
#     temp = digit
#     return temp == rev_digit(digit)
# print("Ans ",palindrome(121))


"""
Q 10 : Reverse String
"""


# def rev_strnig(st, i=0):

#     if i == len(st) - 1:
#         return st[i]

#     return rev_strnig(st, i + 1) + st[i]


# print("ans ",rev_strnig("abc"))


"""
Q 11 : String Palindrome
"""

# def palidrome(st):

#     return st == rev_strnig(st)


# print("ans ",palidrome('abc'))


"""
Q 12 : Find sum of array
"""
# def sum_of_arr(arr,i = 0):
#     if i == len(arr) - 1:
#         return arr[i]

#     return sum_of_arr(arr,i+1) + arr[i]

# print("Ans ",sum_of_arr([1,2,3]))

"""
Q13 : Find maximum element in array
"""
# def max_element(arr:list[int],i = 0,max_elem=0):

#     if i == len(arr):
#         return max_elem

#     if arr[i] > max_elem:
#         max_elem = arr[i]

#     return max_element(arr,i+1,max_elem)

# arr = [1,5,3,22,530,3322,302,320,123,-44]
# print("Ans ",max_element(arr))


"""
Q 14: Find Mininum element in an Array
"""
# def min_element(arr:list[int],i = 0,min_elem=None):
#     if min_elem is None:
#         min_elem = arr[0]

#     if i == len(arr):
#         return min_elem

#     if arr[i] < min_elem:
#         min_elem = arr[i]
#     return min_element(arr,i+1,min_elem)


# arr = [1,5,3,22,530,3322,302,320,123,0]
# print("Answer ",min_element(arr))

"""
Q 15: Check if array is sorted
"""

# def check_sorted(arr:list[int],i = 0,j = 1,ans = True):


#     if j == len(arr):
#         return ans
#     if arr[j] < arr[i]:
#         return False
#     return check_sorted(arr,i+1,j+1,ans)


# arr = [1,3,7,5,6]
# print("Ans ",check_sorted(arr))


"""
Q 16: Linear Search
"""

# def linear_search(arr:list[int],elem,i = 0):
#     if i == len(arr):
#         return -1
#     if arr[i] == elem:
#         return i
#     return linear_search(arr,elem,i+1)


# arr = [5, 10, 15, 20]
# target = 5   # Expected output: index 0
# arr = [2, 4, 6, 8, 10]
# target = 10  # Expected output: index 4
# arr = [100, 200, 300, 400]
# target = 250 # Expected output: -1 (not found)

# print("ans ",linear_search(arr,target))


"""
Q 17 : Find all occurrences of element
"""

# def find_all_occurrences(arr,elem,i=0,res=None):
#     if res is None:
#         res = []
#     if i == len(arr):
#         return res
#     if arr[i] == elem:
#         res.append(i)

#     return find_all_occurrences(arr,elem,i+1,res)


# arr = [2, 4, 2, 6, 2, 8, 2, 10]

# print("Answer ",find_all_occurrences(arr,2))


"""
Q 18: Reverse an array recursively
"""
# def reverse_arr(arr,i = 0,res = None):
#     if res is None:
#         res = []
#     if i == len(arr) - 1:
#         return res
#     res.insert(0,arr[i])
#     return reverse_arr(arr,i+1,res)

# arr = [1,2,3,4]
# print("Ans ",reverse_arr(arr))

# def reverse_arr(arr,i = 0):

#     if i == len(arr):
#         return []

#     rest = reverse_arr(arr,i+1)

#     rest.append(arr[i])
#     return rest
# arr = [1,3,4,5]
# print("Ans ",reverse_arr(arr))


"""
Q 20 : Remove all occurrences of character
"""
# def remove_occ(st,tg,i = 0,res=None):
#     if res is None:
#         res = ""
#     if i == len(st):
#         return res
#     print(st[i])
#     if st[i] != tg:
#         res += st[i]
#     return remove_occ(st,tg,i+1,res)

# st = "apple"
# print("Ans ",remove_occ(st,"p"))


"""
Q 21: Remove consecutive duplicates
"""
# def remove_consec(st,i = 0,j = 1,res = None):

#     if len(st) < 1:
#         return st
#     if res is None:
#         res = ""
#         res += st[i]

#     if j == len(st):
#         return res

#     if st[i] != st[j]:
#         res += st[j]

#     return remove_consec(st,i+1,j+1,res)


# # s = ""
# # s = "x"
# s = "ppppppppq"
# # Expected: ""
# print("Ans ",remove_consec(s))


"""
Q 22 : Replace "pi" with "3.14"
"""


# def replace_pi(st,i = 0,res=""):

#     if i >= len(st):
#         return res

#     if i + 1  < len(st) and st[i] == 'p' and st[i + 1] == 'i':
#         res += "3.14"
#         return replace_pi(st,i+2,res)
#     else:
#         res += st[i]
#         return replace_pi(st,i+1,res)


# st = "piabc"
# # Expected: "abc3.14"
# print("Ans ",replace_pi(st))


"""
Q 23 : Generate all substrings
"""

# def sub_seq(st,start=0,end=1,res = None):
#     if res is None:
#         res = []


#     if start == len(st):
#         return res

#     if end > len(st):
#         return sub_seq(s, start + 1, start + 2,res)
#     res.append(st[start:end])

#     return sub_seq(s,start,end+1,res)


s = "abc"
# Expected substrings: "a", "b", "c", "ab", "bc", "abc"

# print('Ans ',sub_seq(s))


"""
Q 24 Permuation
"""


# def permuation(arr):


#     result = []

#     def backtrack(path,used):


#         if len(path) == len(arr):
#             result.append(path[:])
#             return


#         for i in range(len(arr)):

#             if used[i]:
#                 continue


#             path.append(arr[i])
#             used[i] = True


#             # Explore
#             backtrack(path,used)


#             # undo
#             path.pop()
#             used[i] = False


#     # To track the state or for backtracking
#     used = [False] * len(arr)
#     backtrack([],used)

#     return result


# arr = [1,2,3]
# print("Ans ",permuation(arr=arr))


"""
Q 25 Permuation String
"""

# def permuation(st):

#     result = []

#     def backtrack(path,used):

#         if len(path) == len(st):
#             result.append("".join(path[:]))
#             return

#         for i in range(len(st)):


#             if used[i]:
#                 continue

#             path.append(st[i])
#             used[i] = True

#             # Explore
#             backtrack(path,used)


#             # Undo
#             path.pop()
#             used[i] = False


#     used = [False] * len(st)

#     backtrack([],used)

#     return result


# st = "abc"

# print("Ans ",permuation(st))


"""
Q 26 Binary Search using recursion
"""


# def binary_search(arr, low, high, x):
#     if high >= low:
        
#         mid = low + (high - low) // 2

#         if arr[mid] == x:
#             return mid

#         elif x > arr[mid]:
#             return binary_search(arr, mid + 1, high, x)
#         else:
#             return binary_search(arr, low, mid - 1, x)
#     else:
#         return -1


# arr = [2, 3, 4, 10, 40, 50, 70]
# print("Ans ", binary_search(arr, 0, len(arr) - 1, 3))


# Iterative approach

# def binary_search(arr,x):
    
#     n = len(arr)
    
#     low = 0
    
#     high = n - 1
    
    
#     while low < high:
        
        
#         mid = (high // 2) + 1
        
        
#         if arr[mid] == x:
#             return mid
        
#         elif x > arr[mid]:
            
#             low = mid + 1
#         else:
#             high = mid - 1
            
#     else:
#         return - 1



'''
Q 27: Tower of Hanoi using recursion
'''
# def tower_of_hanoi(n, from_rod, aux_rod, to_rod):

#     if n == 0:
#         return

#     tower_of_hanoi(n - 1, from_rod, to_rod, aux_rod)

#     print("Move disk", n, "from", from_rod, "to", to_rod)

#     tower_of_hanoi(n - 1, aux_rod, from_rod, to_rod)
    

# tower_of_hanoi(3, 'A', 'B', 'C')


'''
Q 28: Josephus Problem (Remove every kth person from list and return the last person)
'''
# def remove_kth_person(arr,k):
#     index = 0
    
#     while len(arr) > 1:
        
#         index = (index + k  - 1) % len(arr)        
        
#         arr.pop(index)
        
#     return arr[0]

# arr = [1,2,3,4,5]
# k = 2

# print("Ans ",remove_kth_person(arr,k))


# Optimized version

# def josephus(n,k):
    
#     if n == 1:
#         return 0
    
#     return (josephus(n - 1,k) + k) % n


# arr = [1,2,3,4,5]
# k = 2

# print("Remaining element is => ",arr[josephus(len(arr),k)])


'''
Q 29 : Count ways to climb stairs
'''


# def ways(n):
    
#     if n <= 1:
#         return 1
#     return ways(n - 1) + ways(n - 2)


# print("Ways ",ways(6))


'''
Q 30 : coin change
'''
# def coin_change(coins,amt,i = 0):
#     if amt == 0:
#         return 1
#     if amt < 0 or i == len(coins):
#         return 0
    
#     take = coin_change(coins,amt - coins[i],i)
#     skip = coin_change(coins,amt,i + 1)
#     return take + skip

# print("Answer ",coin_change([1,2,3],4))




'''
Q 31 : N Queens
'''

# def is_safe(mat,row,col):
#     n = len(mat)
    
#     # check this col on upper side
#     for i in range(len(mat)):
#         if mat[i][col]:
#             return 0
    
#     # check upper diagonal on lef
#     i,j = row - 1,col - 1
#     while i  >= 0 and j >= 0:
#         if mat[i][j]:
#             return 0
#         i -= 1
#         j -= 1
    
#     # check upper diagonal on the right side
#     i, j = row - 1, col + 1
#     while i >= 0 and j < n:
#         if mat[i][j]:
#             return 0
#         i -= 1
#         j += 1
#     return 1

# def place_queens(row,mat,result):
    
    
#     n = len(mat)
    
#     # base case if all queens are placed
#     if row == n:
#         print("base case cliked ")
        
        
#         ans = []
#         for i in range(n):
#             for j in range(n):
#                 if mat[i][j]:
#                     ans.append(j + 1)
#         result.append(ans)
#         print("Result ", result)
#         return
    
#     # Consider the row and try placing in all columns one by one    
#     for i in range(n):
        
        
#         # Check if the queen can be placed 
#         if is_safe(mat,row,i):
#             mat[row][i] = 1
#             place_queens(row + 1,mat,result)
            
            
#             # backtrack 
#             mat[row][i] = 0
            
#     pass
# def n_queens(n):
    
#     # initialize the board
#     mat = [[0] * n for _ in range(n)]
#     result = []
#     place_queens(0,mat,result)
    
#     return result
    
    
    

# print("Answer ", n_queens(4))



'''
Code

Walkthrough

1

Find the pivot

Scan from right to left to find the first position where the sequence stops decreasing. For [1,3,5,4,2], the pivot is 3 because 3 < 5.

2

Find the smallest larger element on the right

Look to the right of the pivot and choose the smallest number that is larger than it. In [1,3,5,4,2], that number is 4.

3

Swap them

Swap the pivot with that larger number.

4

Reverse the suffix

The part to the right is in descending order. Reverse it to make it as small as possible. This guarantees the result is the immediate next permutation.

Example

Input

[1, 3, 5, 4, 2]

Pivot

3

Swap with

4

After swap

[1, 4, 5, 3, 2]

Reverse suffix

[5, 3, 2] → [2, 3, 5]

Result

[1, 4, 2, 3, 5]

Why this is efficient

Find pivot: O(n)

Find swap candidate: O(n)

Reverse suffix: O(n)

Overall time complexity: O(n). Space complexity: O(1).
'''
def next_permuation(nums:list):
    n = len(nums)
    
    # Find the pivot index
    pivot = -1
    for i in range(n - 2,-1,-1):
        if nums[i] < nums[i - 1]:
            pivot = i
            break
    if pivot == -1:
        nums.reverse()
        return
    
    
    for i in range(n - 1,pivot,-1):
        if nums[i] > nums[pivot]:
            nums[i] ,nums[pivot] = nums[pivot],nums[i]
            break
    
    left = pivot + 1
    right = n - 1
    while left <= right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
    
    print("Answer",nums)
arr = [3,2,1]
next_permuation(nums=arr)

