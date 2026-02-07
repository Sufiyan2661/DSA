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

# tc = O(n), sc = O(1)

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

# tc = O(n), sc = O(1)


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


# def to_word(num):
#     word_dict = {
#         "0":"Zero",
#         "1":"One",
#         "2":"Two",
#         "3":"Three",
#         "4":"Four",
#         "5":"Five",
#         "6":"Six",
#         "7":"Seven",
#         "8":"Eight",
#         "9":"Nine"
#     }
#     return word_dict[num]
# num = "986475125"
# for n in num:
#     print("Word ",to_word(n))


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

# tc = O(1) sc = O(1)


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

# tc = O(log n) sc = O(1)


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


# tc = O(n), sc = O(1)

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
tc = O(n)
sc = O(n) because each call stays on the call stack untill base case retuns
"""


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

"""
tc = O(1) ,sc = O(1)
"""

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

"""
Q10: Sum of digits of number
input1 =  687
output = 21
input2 = 12
output = 3
"""
# +++++++++++++++++ (I) iterative approach ++++++++++++++++++++++++
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


"""
Q11 : Program for armstrong numbers
"""

# ++++++++++++++ Naive approach ++++++++++++++++++
# def power(x,y):
#     if y == 0:
#         return 1
#     half = power(x,y//2)
#     if y % 2== 0:
#         return half * half
#     else:
#         return x * half * half

# # function to give the number of digits
# def count(num):
#     num_of_digit = 0
#     n = num
#     while n:
#         num_of_digit += 1
#         n = n // 10
#     return num_of_digit

# def armstrong(num):
#     x = count(num)
#     sum_ = 0
#     temp = num
#     while temp:
#         remainder = temp % 10
#         sum_ += power(remainder,x)
#         temp = temp // 10
#     return sum_ == num

# if __name__ == "__main__":
#     n = 154
#     if armstrong(n):
#         print("True")
#     else:
#         print("False")

# ++++++++++++++ Using Numeric String ++++++++++++++++
# def armstrong(num):
#     num_string = str(num)
#     num_len = len(num_string)
#     output = 0
#     for i in num_string:
#         output += int(i) ** num_len
#     return output == num

"""
tc = O(n) and sc = O(n) because here we are converting given number into string
"""

# if __name__ == "__main__":
#     n = 155
#     if armstrong(n):
#         print("True")
#     else:
#         print("False")

"""
Q 12: Factorial of number 
"""
# +++++++ iterative approach +++++++++
# def factorial(num):
#     ans =1
#     i = 2
#     while i <= num:
#         ans *= i
#         i += 1
#     return ans

"""
while loop runs  from i = 2 to num
thats (num - 1) iterations
each iteration does constant word (*,+=)
tc = O(1) + O(1) + O(n) + O(1) + O(1) = O(n)
sc = O(1) : because here i am using only constant variables except input num 
"""

# if __name__ == "__main__":
#     n = 5
#     print("Factorial ",factorial(n))


# +++++++++++++ Recursive Approach ++++++++++++
# def factorial(n):
#     if n == 0:
#         return 1

#     return n * factorial(n - 1)


"""
tc = time complexity same as above iterative approach  = O(n)
sc = here the game changes because i each recursive call call stack stays in memory till it reaches base case = O(n)
"""

# if __name__ == "__main__":
#     num = 5
#     print("Factorial ",factorial(num))


"""
Q13: Check if an Array is Sorted
"""
# +++++++ Recursive Approach +++++++

# def check_sorted_array(arr:list,arr_len:int):
#     # arr_len = len(arr)
#     if arr_len <= 1:
#         return True
#     return (arr[arr_len -1] >= arr[arr_len - 2] and check_sorted_array(arr,arr_len-1))

"""
operations for tc :
    arr_len = len(arr) takes constant time O(1)
    if arr_len <= 1 takes constant time O(1)
    arr[arr_len -1] >= arr[arr_len - 2] takes constant time O(1)
    check_sorted_array(arr,arr_len-1) here it takes n time because iteration happen till len arr_len  O(n)
    tc = O(1) + O(1) + O(1) + O(n) = O(n)

operation for sc :
    arr_len = len(arr) takes constant space O(1)
    check_sorted_array(arr,arr_len-1) here is case happens for sc because call stack stays in memory till it reaches base case
    tc = O(1) + O(n) = O(n)  
    
"""


# if __name__ == "__main__":
#     arr = [1,3,4,5]
#     if check_sorted_array(arr,len(arr)):
#         print("Sorted")
#     else:
#         print("not sorted")


# ++++++++ Iterative Approach ++++++++++

# def check_sorted_array(arr:list):
#     n = len(arr)
#     if len(arr) <= 1:
#         return True

#     for i in range(1,n):
#         if arr[i-1] > arr[i]:
#             return False
#     return True

"""
operations for tc:
    n = len(arr) takes constant time O(1)
    for i in range (1,n) takes n times to perform because here i am iterating till length of array and the worst case it can iterate upto n number of lements O(n)
    if arr[i - 1] > arr[i] takes constant time O(1)
    return also takes constatn time O(1)
    tc = O(1) + O(n) + O(1) + O(1) = O(n)

operations for sc:
    n = len(arr) takes constant space O(1)
    sc = O(1) 
"""


# if __name__ == "__main__":

#     arr = [1,4,3,4]
#     if check_sorted_array(arr):
#         print("Sorted")
#     else:
#         print("Not Sorted")


"""
Q14: program for multiplication table
"""

# ++++++++++ iterative approach ++++++++++++++++

# def table(n):
#     if n <= 0:
#         return 1
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")


"""
operations for tc:
    for  i in range(1,11) this constant times because it performs multiplication only ten times  O(1)
    tc = O(1)

operations for sc:
    i variables taking only for iteration no extra space taken O(1)
    sc = O(1)
"""
# if __name__ == "__main__":
#     n = 999
#     table(n)


# ++++++++++++++ Recursive Approach ++++++++++++++
# def table(n,i = 1):
#     if i == 11:
#         return
#     print(f"{n} * {i} = {n*i}")
#     i += 1
#     return table(n,i)

"""
tc = O(1)
sc = O(1)
"""

# if __name__ == "__main__":
#     n = 6
#     table(n)


"""
Q15: check if a word is present in the sentence
"""
# def check_word(sentence:str,word:str)->bool:
#     sentence_list = sentence.lower().split(" ")
#     return  word.lower() in sentence_list

"""
operations for tc:
    .lower() takes n times to perform operation because it iterate linearly and perform upto n time iteration O(n)
    .split() takes also n times to perform operation because it iterate linearly to split the sentence
    tc = O(n) + O(n) = O(2n)
    tc = O(2n) so we usually ignore the contant number for calculating tc so tc becomes O(n)
    tc = O(n)
operations for sc:
    sentence_list = sentence.lower().split(" ") takes n number of space so sc is O(1)
    sc = O(1)
"""

# if __name__ == "__main__":
#     sentence = "Geeks for Geeks"
#     word = "or"
#     if check_word(sentence=sentence,word=word):
#         print("Yes")
#     else:
#         print("No")


"""
Q16: Segregate 0 and 1 in array
"""

# ++++++++++++++= Two Traversal ++++++++++++++++++
# def segregate_zero_and_one(arr:list,n:int):
#     count = 0
#     for i in range(0,n):
#         if arr[i] == 0:
#             count += 1

#     # Loop to fill the array with zero until count become
#     for i in range(0,count):
#         arr[i] = 0


#     # Fill the remaining space with 1 in the array
#     for i in range(count,n):
#         arr[i]  = 1


# def print_segregated_array(arr,n):
#     print("Array after segregation is = ",end=" ")
#     for i in range(0,n):
#         print(arr[i] , end=" ")

"""
operations perform in segregate_zero_an_one for tc:
    count = 0 takes constant times O(1)
    for i in range(0,n) takes n times and perform constant operation in each iteration O(n)
    for i in rnage(0,count) it can takes upto n times if the list has only 0s in the list  so it takes  O(n) times
    for i in range(count,n) it can also takes upto n times if the list has only 1s i the list so it takes O(n) times
    tc = O(1) + O(n) + O(n) + O(n) = O(3n)
    tc = O(n) because we usually ignore the constant values
operations perform in segregate_zero_an_one for sc:
    count = 0 here we are taking only one variables to do iteration O(1)
    sc = O(1)


operations perform in print_segregated_array for tc:
    for i in range(0,n) it takes also n times to iterate O(n)
    tc = O(n)
    
operations perform in print_segregated_array for sc:
    initializing i for iteratation takes constant space O(1)
    sc = O(1)  

"""


# if __name__ == "__main__":
#     arr = [ 0, 1, 0, 1, 1, 1 ]
#     n = len(arr)
#     segregate_zero_and_one(arr,n)
#     print_segregated_array(arr,n)


# +++++++++++ One Traversal ++++++++++++++++++
# def segregate_zero_and_one(arr:list,n:int):
#     low_index = 0
#     high_index = n-1

#     while low_index < high_index:


#         # increment the value of low_index till you find 0
#         while arr[low_index] == 0 and low_index < high_index:
#             low_index += 1


#         # decrement the value of high_index till you find 1
#         while arr[high_index] == 1 and low_index < high_index:
#             high_index -= 1

#         if low_index < high_index:
#             arr[low_index],arr[high_index] = arr[high_index],arr[low_index]


"""
operations for tc:
   low_index = 0          → O(1)
high_index = n - 1     → O(1)
while low_index < high_index → total pointer movements ≤ n → O(n)
    while arr[low_index] == 0 → total moves ≤ n → O(n)
    while arr[high_index] == 1 → total moves ≤ n → O(n)
    swap → total swaps ≤ n/2 → O(n)
    tc = O(1) + O(1) + O(n) + O(n) + O(n) = O(n)
    
operations for sc:
    low_index = 0 takes constant space O(1)
    high_index = -1 takes constant space O(1)
    sc = O(1)    
"""
# if __name__ == "__main__":
#     arr = [0, 1, 0, 1, 1, 1]
#     segregate_zero_and_one(arr,len(arr))
#     print("Array after segregation using one traversal ",arr)


"""
Q17: Write a program to divide array or list in given numbers
"""
# class DivideList:
#     def __init__(self,arr:list,n:int):
#         self.arr = arr
#         self.n = n
#         self.result = []
#         self.num_of_list = self.number_of_list()
#     def number_of_list(self) -> int:
#         length = len(self.arr)
#         # result = []
#         start = 0

#         for i in range(self.n):
#             part_size = length // self.n + (1 if i < length % self.n else 0)
#             self.result.append(self.arr[start:start + part_size])
#             start += part_size

#         return len(self.result)

#     def get_given_list(self,n:int) -> list:
#         return self.result[n]


# if __name__ == "__main__":
#     li = [1,2,3,4,3,2,4,5,5,7,94,9,13,6]
#     four_pages = DivideList(li,4)

#     print("Number of lists ",four_pages.num_of_list)


#     print("Given List ",four_pages.get_given_list(3))

"""
Q18: write a program to reverse digits of numbers
"""

# +++++++++ iterative approach ++++++++++++++++++
# def reverse_digits(num:int) -> int:
#     n = num
#     reverse_num = 0
#     while n != 0:
#         reverse_num = reverse_num * 10 + n % 10
#         n = n // 10
#     return reverse_num


"""
oporations for tc:
    n = num                  → O(1)   (assign variable)
    reverse_num = 0          → O(1)   (assign variable)

    while n != 0:            → O(log n)  
    reverse_num = reverse_num * 10 + n % 10   → O(1) per iteration
    n = n // 10                               → O(1) per iteration
    return reverse_num       → O(1)
    tc =  O(1) + O(1) + O(log n) + O(1) + O(1) 
    tc = O(log n) 
    
operation for sc:
    reverse_num = 0 takes constant space O(1)
    sc = O(1)

"""

# if __name__ == "__main__":
#     num = 200
#     print("Reversed number ",reverse_digits(num=num))

# +++++++++++++ Recursive approach ++++++++++++++++++++
# def reverse_digits(num:int, rev_num:int,base_pos:int):
#     if num > 0:
#         reverse_digits(num//10,rev_num,base_pos)
#         rev_num[0] += (num % 10) * base_pos[0]
#         base_pos[0] *= 10

"""
operations for tc:
    reverse_digits(num//10,rev_num,base_pos)  -> O(log n)
    rev_num[0] += (num % 10) * base_pos[0]  -> O(1)
    base_pos[0] *= 10 -> O(1)
    tc = O(log n) + O(1) + O(1)
    tc = O(log n)
operations for sc:  
    
    
    
"""


# if __name__ == "__main__":
#     num = 123
#     rev_num = [0]
#     base_pos = [1]
#     reverse_digits(num=num,rev_num=rev_num,base_pos=base_pos)
#     print("Reverse num ",rev_num)


# def reverse_digits(num: int, reverse_num: int = 0) -> int:
#     if num == 0:
#         return reverse_num
#     reverse_num = reverse_num * 10 + num % 10
#     return reverse_digits(num // 10, reverse_num)

"""
operations for tc:
    reverse_num = reverse_num * 10 + num % 10 it takes constant time O(1)
    reverse_digits(num // 10, reverse_num) this takes log10n where n is the num and 10 by which i am dividing so tc for this line become O(log n)
    tc = O(1) + O(log n) = O(log n)
operation for sc:
    reverse_num = reverse_num * 10 + num % 10 this takes constant space O(1)
    reverse_digits(num // 10, reverse_num) this takes space of O(log n) because for each recursive call the call stack stays in the memory till reches bas case
    sc = O(1) + O(log n) = O(log n)
    
"""


# if __name__ == "__main__":
#     num = 123
#     print("Reversed number ", reverse_digits(num=num))


"""
Q18: Second largest element in an array
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34

Input: arr[] = [10, 5, 10]
Output: 5

Input: arr[] = [10, 10, 10]
Output: -1
"""

# +++++++++++ Sorting approach (Ascending order) +++++++++++++
# def second_largest(arr:list):
#     n = len(arr)
#     arr.sort()

#     for i in range(n - 2,-1,-1):

#         if arr[i] != arr[n -1]:
#             return arr[i]
#         return -1

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
#     arr = [12, 35, 1, 10, 34, 1]
#     print("Second largest element ",second_largest(arr=arr))

# ++++++++++++ Two pass search approach ++++++++++++++++++
# def second_largest(arr:list):
#     largest_element = -1
#     second_largest_element = -1
#     for element in arr:
#         if element > largest_element:
#             largest_element = element
#     for element in arr:
#         if element > second_largest_element and element != largest_element:
#             second_largest_element = element

#     return second_largest_element


"""
operations for tc:
    largest_element = -1 takes constant time O(1)
    second_largest_element = -1 takes constant time O(1)
    for element in arr :firlst loop -> it can takes n number of times because it is iterating each element and performing constant operation in each iteration. O(n)
    for element in arr : second loop -> it can also takes O(n)
    return takes O(1)
    tc = O(1) + O(1) + O(n) + O(n) + O(1) = O(2n)
operations for sc:
    largest_element = -1 takes constant space O(1)
    second_largest_element = -1 takes constant space O(1)
    element for iteration takes constant space in each iteration O(1)
    sc = O(1)    
"""
# if __name__ == "__main__":
#     arr = [10, 10, 10]
#     print("Second largest element ",second_largest(arr=arr))


# ++++++++++++++++++ One pass Search +++++++++++++++++++++
# def second_largest(arr:list):
#     largest_element = -1
#     second_largest_element = -1
#     arr_len = len(arr)
#     for i in range(0,arr_len,1):

#         # if arr[i] is greater than largest_element the second_largest_element = largest_element and largest_element = arr[i]
#         if arr[i] > largest_element:
#             second_largest_element = largest_element
#             largest_element = arr[i]

#         elif arr[i] < largest_element and arr[i] > second_largest_element:
#             second_largest_element = arr[i]
#     return second_largest_element

'''
operations for tc:
    here in each linear iteration i am performing constant operations so the time complexity of this approach is O(n)
    tc = O(n)
operations for sc:
    here i am taking only two variables for storing largest and second largest element so space complexity of this approach is O(1)
    sc = O(1)
'''

# if __name__ == "__main__":
#     arr = [12, 35, 1, 10, 34, 1]
#     print("Second largest element in the array ",second_largest(arr=arr))


"""
Q19: Factor of given number
"""

# +++++++++ iterative approach =+++++++++++++++++
# def factors_of_number(num:int)->list:
#     n = 1
#     result = []
#     while n <= num:
#         if num % n == 0:
#             result.append(n)
#         n += 1
#     return result
# if __name__ == "__main__":
#     num = 10
#     print(f"Factors of number {num} is =>  ",factors_of_number(num=num))

'''
operaitons for tc:
    while n <= num: → iterates from 1 to num → num iterations = O(num)
    num % n == 0 → modulo is O(1)
    result.append(n) → appending to a list is amortized O(1)
So each iteration is O(1), and we do num iterations, hence:
    tc = O(n) + O(1) = O(n)
operations for sc:

'''


# # ++++++++++++ Better approach (loop only till the half of the given number) ++++++++++++++
# def factors_of_number(num:int) -> list:
#     result = []
#     for i in range(1,(num//2)+1):
#         if num % i == 0:
#             result.append(i)
#     result.append(num)
#     return result
'''
operations for tc:
    for i in range(1,(num//2)+1) -> takes n/2 iteration for constant operation inside loop
'''

# if __name__ == "__main__":
#     num = 36
#     print("Factors of given number is ",factors_of_number(num=num))

# ++++++++++++++++++ optimal approach +++++++++++++++++++++++++
# from math import sqrt
# def factors_of_number(num:int) -> list:
#     result  = []
#     for  i in range(1,int(sqrt(num))+1):
#         if num  % i == 0:
#             result.append(i)

#             if num // i != i:
#                 result.append(num//i)
#     result.sort()
#     return result

# if __name__ == "__main__":
#     num = 36
#     print("Factor of numbers are ",factors_of_number(num=num))
