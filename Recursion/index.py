'''
Q 1 Print number from 1 to n
'''
# def print_number(n, i = 1):
#     if i > n:
#         return
#     print(i)
#     print_number(n,i+1)

# print_number(5)


'''
Q2 : Print numbers from N to 1
'''
# def n_to_one(n):
#     if n == 0:
#         return 
#     print(n)
#     n_to_one(n -1)


# n_to_one(5)


'''
Q3 : . Sum of first N natural numbers
'''

# def sum_of_n(n):
#     if n == 1:
#         return 1
#     return n + sum_of_n(n - 1)

# print("ans ",sum_of_n(5))


'''
Q 4: Factorial of a number
'''
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# print("Ans ",fact(4))

'''
Q 5: Power function
'''

# def power(n,pow):
#     if pow == 1:
#         return n
#     return n * power(n,pow - 1)

# print("ans ",power(2,5))

'''
Q 6: Count digits in a number
'''
# def count_digit(digit,count = 0):
#     if digit == 0 and count == 0:
#         return 1
#     if digit == 0:
#         return count
#     return count_digit(digit// 10,count + 1)


# print("ans ",count_digit(0))


'''
Q 7:  Sum of digits
'''
# def sum_of_digits(digit,sm = 0):
#     if digit == 0 and sm == 0:
#         return -1
#     if digit == 0:
#         return sm
#     sm += digit % 10
#     return sum_of_digits(digit// 10,sm)

# print("ans ",sum_of_digits(1))    


'''
Q 8: REverse digit
'''
# def rev_digit(digit,rev = 0):
#     if digit == 0:
#         return rev
#     rev = (rev * 10) + digit % 10
#     return rev_digit(digit // 10,rev)


# print('Ans ',rev_digit(123))

'''
Q 9 : Check palindrome number/string
'''
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


'''
Q 10 : Reverse String
'''

def rev_strnig(st,i = 0):
    
    if i == len(st) - 1:
        return st[i]
    
    return rev_strnig(st,i+1) + st[i]

# print("ans ",rev_strnig("abc"))


'''
Q 11 : String Palindrome
'''

# def palidrome(st):
    
#     return st == rev_strnig(st)
    


# print("ans ",palidrome('abc'))


'''
Q 12 : Find sum of array
'''
# def sum_of_arr(arr,i = 0):
#     if i == len(arr) - 1:
#         return arr[i]
    
#     return sum_of_arr(arr,i+1) + arr[i]

# print("Ans ",sum_of_arr([1,2,3]))

