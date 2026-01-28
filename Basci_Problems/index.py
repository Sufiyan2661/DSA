# count odd and even
"""Q 1:- you are given an array arr[]. Your task is to count the number of even and odd elements.Return first odd count then even count."""


# APPROACH :- By using mod operator
# def count_odd_even(arr):
#     odd_count = 0
#     even_count = 0

#     # iterate
#     for num in arr:

#         # check if it is even
#         if num % 2 ==0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return odd_count,even_count


# APPROACH :- By using & Operator
# def count_odd_even(arr):
#     count_even = 0
#     count_odd = 0
#     for num in arr:
#         if num & 1:
#             count_even +=1
#         else:
#             count_odd += 1
#     return count_odd,count_even
# if __name__ == "__main__":
#     input_1 = [2,3,4,5,6]
#     output = count_odd_even(input_1)
#     print(output[0], output[1])


"""
Q2: Given an array the task is to find average of that array.Average is the sum of array eleens divided by the number of elements.
"""

#
# def average(arr:list):
#     if len(arr) == 0:
#         return "array can`t be empty "

#     total = sum(arr)
#     total_num_of_elements = len(arr)
#     return total/total_num_of_elements

# print("The sum of array ",average([1,2,3,4,5]))


"""
Q3 : Number extraction
"""

# using while

# n = 4857
# num = n
# while num > 0:
#     last_digit = num % 10
#     print("The last digit ",last_digit)
#     num = num//10

# Using Recursion
# def extract_digits(n):
#     if n == 0:
#         return
#     print("last digit",n % 10)
#     return extract_digits(n//10)


"""
Q4: Program to print given numbers in word
"""
# def to_word(num):

#     if num == 0:
#         return "Zero"
#     elif num == 1:
#         return "One"
#     elif num == 2:
#         return "Two"
#     elif num == 3:
#         return "Three"
#     elif num == 4:
#         return "Four"
#     elif num == 5:
#         return "Five"
#     elif num == 6:
#         return "Six"
#     elif num == 7:
#         return "Seven"
#     elif num == 8:
#         return "Eight"
#     elif num == 9:
#         return "Nine"
# num = "986475125"
# for n in num:
#     print("Word ",to_word(int(n)))


"""
Q5:Check if large number is divisible 6 or not

input1 : n = 2112
output : yes
input2 : n = 1124
output : no
input3 : 363588395960667043875487
output : no
"""


# def div_by_six(n):
#     if n % 6 == 0:
#         return "Yes"
#     else:
#         return "No"


# print("divisible by six ",div_by_six(2112))
# print("\ndivisible by six ",div_by_six(1124))
# print("\ndivisible by six ",div_by_six(363588395960667043875487))


# def check(st):


#     n = len(st)


#     if (((int)(st[n-1])%2) != 0) :
#         return False


#     digit_sum = 0
#     for i in range(0,n):
#         digit_sum = digit_sum + (int)(st[i])


#     return (digit_sum % 3 == 0)


# st= "1234"
# if check(st):
#     print("Yes")

# else:
#     print("No")


"""'
Q6 Check Palindrome
Input: n = 12321
Output: True
Explanation: 12321 is a palindrome number because it reads same  forward and backward.

Input: n = 1234
Output:  False
Explanation: 1234 is not a palindrome number because it does not read the same forward and backward.
"""

# def palindrome(n):
#     num = n
#     reverse = 0
#     while num != 0:
#         reverse = (reverse * 10) + (num % 10)
#         num = num // 10

#     return n == reverse

# if palindrome(1234):
#     print("Yes")
# else:
#     print("No")


"""
Q7 Program to count vowels in a string 
"""
# (I) Iterative approach

# def count_vowels(st):
#     count = 0
#     for char in st:
#         if char.lower() in ['a','e','i','o','u']:
#             count += 1
#     return count


# print("Vowels in string ",count_vowels("ABC DE"))

# (II) Recursive approach
# def vowels(ch):
#     return ch.lower() in ['a','e','i','o','u']

# def count_vowels(str,n):
#     '''
#     Docstring for count_vowels

#     :param str: String
#     :param n: length of that string
#     '''
#     if n == 1:
#         return vowels(str[n-1])
#     return (count_vowels(str,n-1) + vowels(str[n-1]))
# st = 'abc de'
# print("total vowels ",count_vowels(st,len(st)))


"""
Q8 Check if a given number is perfect square
input = 36
output = yes
input = 2500
output = yes

"""
# import math
# def perfect_sqrt(n):

#     if n > 0:
#         sqrt = math.sqrt(n)

#         return sqrt * sqrt == n

#     return False


# print("Sqrt ",perfect_sqrt(2500))


"""
Q9 : Program to find the maximum element in the matrix
input1 = > [
    [1,2,3,4],
    [25, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
output = 25
input2 =[
    [9, 8, 7, 6],
    [5, 4, 3, 2],
    [1, 0, 12, 45]
] 
output = 45
"""
# def max_elem_from_matrix(matrix: list):
#     max_element = 0
#     for outer in matrix:
#         for inner in outer:
#             if inner > max_element:
#                 max_element = inner
#     return max_element
# matrix1 = [[1, 2, 3, 4], [25, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# matrix2 = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, 12, 45]]
# print("Maximum element of matrix 1 ", max_elem_from_matrix(matrix=matrix1))
# print("Maximum element of matrix 2 ", max_elem_from_matrix(matrix=matrix2))

'''
Q10: Sum of digits of number
input1 =  687
output = 21
input2 = 12
output = 3
'''
#+++++++++++++++++ (I) iterative approach ++++++++++++++++++++++++
# def sum_of_nums(num:int):
#     n = num
#     num_sum = 0
#     while n!= 0:
#         num_sum += n % 10
#         n = n // 10
#     return num_sum

# num1 = 687
# num2 = 12
# print("sum of input 1 ",sum_of_nums(num1))
# print("sum of input 2 ",sum_of_nums(num2))



# +++++++++++++++++++ Recursive Approach +++++++++++++++++++++++
# def sum_of_nums(nums:int):
#     n = nums
#     if n == 0:
#         return 0
    
#     return n % 10 + sum_of_nums(n // 10)

# num1 = 687
# num2 = 12
# print("sum of input 1 ",sum_of_nums(num1))
# print("sum of input 2 ",sum_of_nums(num2))
    

'''
Q11 : 
'''