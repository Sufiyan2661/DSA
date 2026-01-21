# Q 1:- Given a number number n, check it is even or not , if even return true else false
# def even_or_odd(n):
    # +++++++ First way +++++
    # if not n:
    #     return -1
    # if n%2==0:
    #     return True
    # return False

    # +++++++++ Second +++++++++

#     return n % 2 == 0



# With bitwise AND 

# def even_or_odd_with_bitwise_and(n):
#     return n & 1 == 0

# print("Even number ",even_or_odd_with_bitwise_and(2))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Q 2:- Given a number n we need to print its table
# def table(n):
#     if not n:
#         return
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")
        

# table(5)

# Recursive approach
# def table(n,i=1):
#     if i == 11:
#         return
#     print(f"{n} * {i} = {n*i}")

#     i += 1
#     table(n,i)
# table(5)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Q 3:- Given a positive integer n 