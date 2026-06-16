"""
Q1 lareget substring palindrome
"""

s = "babad"


# def expan_from_center(left,right):
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1

#     return s[left + 1:right]


# largest = s[0]

# for i in range(len(s) - 1):
#     odd = expan_from_center(i,i)

#     even  = expan_from_center(i,i+ 1)

#     if len(odd) > len(largest):
#         largest = odd
#     if len(even) > len(largest):
#         largest = even


# '''
# tc = O(n^2)
# sc = O(1)
# '''

# print(largest)

"""
Q 2 : Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""
# x = 123

# new_num = 0
# while x:


#     new_num = (new_num * 10) + (x % 10)


#     x = x // 10


#     print(new_num)


# mini = -2147483648
# maxi = 2147483647
# if new_num < mini or new_num > maxi:
#     print(0)
# else:
#     print(new_num)

"""
3. Container With Most Water
input = [1,8,6,2,5,4,8,3,7]
output = 49
"""

# def max_water(heights:list[int])->int:

#     left = 0
#     right = len(heights) - 1

#     curr_max = 0

#     while left < right:

#         width = right - left

#         area = min(heights[left],heights[right]) * width

#         curr_max = max(curr_max,area)

#         if heights[left] < heights[right]:
#             left += 1

#         else:
#             right -= 1

#     return curr_max

# if __name__ == "__main__":
#     arr = [1,8,6,2,5,4,8,3,7]

#     print("max water ",max_water(heights=arr))

"""
Q3 Integer to Roman
input = 3749
output = "MMMDCCXLIX"
"""


# if __name__ == "__main__":
#     print("Roman ", int_to_roman(58))


"""
Q4 Roman to integer
"""


# def roman_to_int(s):
#     roman_map = {
#         "M": 1000,
#         "CM": 900,
#         "D": 500,
#         "CD": 400,
#         "C": 100,
#         "XC": 90,
#         "L": 50,
#         "XL": 40,
#         "X": 10,
#         "IX": 9,
#         "V": 5,
#         "IV": 4,
#         "I": 1,
#     }
#     new_val = 0
#     i = 0

#     while i < len(s):
#         if i + 1 < len(s) and s[i] + s[i + 1] in roman_map:
#             new_val += roman_map[s[i]+s[i + 1]]
#             i += 2
#         else:
#             new_val += roman_map[s[i]]
#             i += 1
#     return new_val
# if __name__ == "__main__":
#     # s = "LVIII"
#     s = "MCMXCIV"


#     print("value ",roman_to_int(s=s))


"""
Q 5 Largest Prefix
"""


# def largest_prefix(strs:list[str])->str:

#     n = len(strs)
#     strs = sorted(strs)
#     print("Sorted ",strs)

#     first = strs[0]
#     last  = strs[n - 1]

#     ans = ""
#     minimum = min(len(first),len(last))
#     for i in range(minimum):
#         if first[i] != last[i]:
#             return ans
#         ans += first[i]
#     return ans


# if __name__ == "__main__":
#     strs = ["flower","flow","flight"]
#     print("Prefix ",largest_prefix(strs=strs))


"""
Q 6 3Sum
"""

# def three_sum(arr:list)->list:

#     arr.sort()
#     n = len(arr)
#     new_arr = []
#     for i in range(n):

#         # skip the duplicates
# if i > 0 and arr[i] == arr[i -1]:
#     print("arr of i ",arr[i], " arr[i - 1] ",arr[i - 1])
#     print("in continue")
#     continue

#         left = i + 1
#         right = n - 1
#         while left < right:

#             t_sum = arr[i] + arr[left] + arr[right]

#             if t_sum < 0 :
#                 left += 1

#             if t_sum > 0:
#                 right -= 1

#             if t_sum == 0:
#                 new_arr.append([arr[i],arr[left],arr[right]])
#                 left += 1
#                 right -= 1

# while left < right and arr[left] == arr[left + 1]:
#     left += 1
# while left < right and arr[right] == arr[right - 1]:
#     right -= 1
#     print("New Arr ",new_arr)


# if __name__ == "__main__":

#     # arr = [-1,0,1,2,-1,-4]
#     arr = [1,2,0,1,0,0,0,0]

#     three_sum(arr=arr)

"""
Q 7 3Sum

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
# def three_sum(arr:list,tgt:int) -> int:

#     arr.sort()
#     n = len(arr)
#     for i in range(n):


#         left = i + 1
#         right = n - 1

#         while left < right:

#             t_sum = arr[i] + arr[left] + arr[right]
#             print("Sum ",t_sum)
#             if t_sum < tgt:
#                 left += 1
#             elif t_sum > tgt:
#                 right -= 1
#             elif t_sum == tgt:
#                 left += 1
#                 right -= 1
#         if tgt > 0 and t_sum > 0:
#             return t_sum


# if __name__ == "__main__":
#     arr = [-1,2,1,-4]
#     target = 1
#     ans = three_sum(arr,target)
#     print("Ans ",ans)


"""
Q 8: Letter Combinations of a Phone Number
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

# p_n_dict = {
#     "2":"abc",
#     "3":"def",
#     "4":"ghi",
#     "5":"jkl",
#     "6":"mno",
#     "7":"pqrs",
#     "8":"tuv",
#     "9":"wxyz"
# }

# def letter_combination(digits:str)->list:

#     if digits is None:
#         return []

#     result = [""]

#     for digit in digits:

#         letters = p_n_dict[digit]
#         new_result = []
#         for combination in result:
#             for letter in letters:
#                 new_result.append(combination + letter)
#         result = new_result

#     return result


# if __name__ == "__main__":
#     print("Ans => ",letter_combination("3"))


"""
Q 9 : 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""


# def four_some(arr:list,target)->list:
#     arr.sort()
#     n = len(arr)
#     result = []
#     for i in range(n):
#         for j in range(i+1,n):

#             left = j + 1
#             right = n - 1

#             while left < right:
#                 curr_sum = arr[i] + arr[j] + arr[left] + arr[right]

#                 if curr_sum < target:
#                     left += 1
#                 elif curr_sum > target:
#                     right -= 1

#                 else:
#                     result.append([arr[i],arr[j],arr[left],arr[right]])
#                     left += 1
#                     right -= 1

#     return result

# if __name__ == "__main__":
#     nums = [1,0,-1,0,-2,2]
#     target = 0
#     print("Ans ",four_some(nums,target))

"""
Q 10 Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# def print_list(head):
#     curr = head
#     while curr:
#         print(curr.data,end='')
#         if curr.next:
#             print(' --> ',end='')
#         curr = curr.next
#     print()


# def remove_element(head,num = 2):
#     curr = head
#     length = 0
#     if curr.next is None:
#         return head

#     while curr:
#         length += 1
#         curr = curr.next

#     target = length - num
#     curr = head
#     i = 1
#     while curr and i < target:
#         print(i)
#         curr = curr.next
#         i = i + 1
#     print("elem ",curr.data)
#     curr.next = curr.next.next
#     print("next data ",curr.data)
#     return head


# if __name__ == "__main__":
#     head = Node(1)
#     # head.next  = Node(2)
#     # head.next.next = Node(3)
#     # head.next.next.next = Node(4)
#     # head.next.next.next.next = Node(5)


#     head = remove_element(head)


#     print_list(head=head)


"""
Q 11 : Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


# class Stack:
#     def __init__(self, capacity):

#         self.arr = [0] * capacity

#         self.capacity = capacity

#         self.top = -1

#     def is_empty(self):
#         return self.top == -1

#     def is_full(self):

#         return self.top == self.capacity - 1

#     def push(self, value):
#         if self.is_full():
#             return
#         self.top += 1
#         self.arr[self.top] = value

#     def pop(self):
#         if self.is_empty():
#             return None
#         value = self.arr[self.top]
#         self.top -= 1
#         return value

#     def peek(self):
#         if self.is_empty():
#             return None

#         return self.arr[self.top]


# def is_valid(s: str) -> bool:
#     stack = Stack(len(s))
#     mapping = {")": "(", "}": "{", "]": "["}

#     for ch in s:


#         # if closing bracket
#         if ch in mapping:

#             if stack.is_empty():
#                 return False

#             top = stack.peek()

#             if mapping[ch] == top:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.push(ch)

#     return stack.is_empty()


# if __name__ == "__main__":
#     s = "(]"
#     print("Ans => ",is_valid(s))


"""
Q 12 : Merge two sorted linked list
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""


# class Node:
#     def __init__(self,data = 0):
#         self.data = data
#         self.next = None


# def merge_list(l1:Node,l2:Node) -> Node:
#     l3 = Node()

#     tail = l3
#     while l1 and l2:

#         if l1.data < l2.data:
#             tail.next = l1
#             l1 = l1.next
#         else:
#             tail.next = l2
#             l2 = l2.next
#         tail = tail.next

#     if l1:
#         tail.next = l1
#     else:
#         tail.next = l2

#     return l3.next


# def print_list(head:Node) -> None:

#     curr = head

#     while curr:

#         print(curr.data,end="")
#         if curr.next:
#             print(" --> ",end="")
#         curr = curr.next
#     print()


# if __name__ == "__main__":
#     l1 = Node(1)
#     l1.next = Node(2)
#     l1.next.next = Node(4)


#     l2 = Node(1)
#     l2.next = Node(3)
#     l2.next.next = Node(4)

#     head = merge_list(l1=l1,l2=l2)
#     print_list(head=head)


"""
Q 14 : Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 
"""


# def remove_duplicates(arr:list) ->int:

#     n = len(arr)

#     i = 0
#     for j in range(n):
#         if arr[j] != arr[i]:
#             i += 1
#             arr[i] = arr[j]
#     return i + 1


# if __name__ == "__main__":
#     arr = [0,0,1,1,1,2,2,3,3,4]
#     k = remove_duplicates(arr=arr)

#     for i in range(k):
#         print(arr[i],end=" ")


"""
Q 15 : Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 
"""

# def remove_element(arr:list,val:int) -> int:
#     n = len(arr)

#     i = 0
#     remove_count = 0
#     while i < n:
#         if arr[i] == val:
#             arr.pop(i)
#             arr.append("_")
#             i -= 1
#             remove_count +=1
#         else:
#             i += 1
#     return n - remove_count

# if __name__ == "__main__":
#     arr = [0,1,2,2,3,0,4,2]
#     val = 2
#     k = remove_element(arr=arr,val=val)
#     for i in range(k):
#         print(arr[i],end=" ")


"""
Q 16: Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
# class Node:
#     def __init__(self,data= 0):
#         self.data = data
#         self.next = None


# def print_list(head):
#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next:
#             print(' --> ',end="")
#         curr = curr.next
#     print()

# def reverse_k_group(head,k):
#     dummy = Node()
#     dummy.next = head
#     group_prev = dummy

#     while True:

#         # Find the kth node
#         kth = group_prev
#         for _ in range(k):
#             kth = kth.next
#             if not kth:
#                 return dummy.next

#         group_next = kth.next
#         prev = group_next
#         curr = group_prev.next
#         while curr != group_next:

#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp

#         temp = group_prev.next
#         group_prev.next = kth
#         group_prev = temp
#     return dummy.next


# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)

#     print_list(head=head)
#     head = reverse_k_group(head,2)
#     print_list(head=head)


"""
Q 17 : Given the head of a linked list, rotate the list to the right by k places.
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

# class Node:
#     def __init__(self,data = 0):
#         self.data = data
#         self.next = None


# def move_to_left(head:Node,k:int) -> Node:

#     if not head or k == 0:
#         return head

#     curr = head


#     length = 1
#     while curr.next:
#         length += 1
#         curr = curr.next

#     last = curr
#     k = k % length
#     if k == 0:
#         return head
#     curr = head

#     for _ in range(length - k - 1):
#         curr = curr.next

#     new_head = curr.next
#     curr.next = None
#     last.next = head

#     return new_head


# def print_list(head:Node) -> None:
#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next:
#             print("-->",end=" ")
#         curr = curr.next
#     print()


# if __name__ == "__main__":

#     head = Node(1)
#     head.next = Node(2)
#     # head.next.next = Node(3)
#     # head.next.next.next = Node(4)
#     # head.next.next.next.next = Node(5)

#     # print_list(head=head)
#     head = move_to_left(head=head,k=2)
#     print_list(head=head)

"""
Q 18 : Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head =  [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""
# class Node:
#     def __init__(self,data = 0):
#         self.data = data
#         self.next = None


# def print_list(head:Node) -> Node:

#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next:
#             print("-->",end=" ")
#         curr = curr.next

#     print()


# def remove_duplicates(head:Node) -> Node:
#     dummy = Node()
#     dummy.next = head
#     prev = dummy
#     curr = head
#     while curr:
#         if curr.next and curr.data == curr.next.data:
#             duplicate_value = curr.data

#             while curr and curr.data == duplicate_value:
#                 curr = curr.next

#             prev.next = curr
#         else:

#             prev = curr
#             curr = curr.next

#     return dummy.next

# # [1,2,3,3,4,4,5]
# if __name__ == "__main__":

#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(3)
#     head.next.next.next.next = Node(4)
#     head.next.next.next.next.next = Node(4)
#     head.next.next.next.next.next.next= Node(5)


#     print_list(head=head)
#     head = remove_duplicates(head=head)
#     print_list(head=head)


"""
Q 19 : Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
# class Node:
#     def __init__(self,data = 0):
#         self.data = data
#         self.next = None


# def print_list(head:Node) -> None:
#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next:
#             print('-->',end=" ")
#         curr = curr.next
#     print()

# def remove_duplicates(head:Node) -> Node:

#     curr = head
#     while curr and curr.next:
#         if curr.data == curr.next.data:
#             curr.next = curr.next.next
#         else:
#             curr = curr.next
#     return head


# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(1)
#     head.next.next = Node(2)

#     print_list(head=head)
#     head = remove_duplicates(head=head)
#     print_list(head=head)


"""
Q 20 : Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
"""

# class Node:
#     def __init__(self,data = 0):
#         self.data = data
#         self.next = None

# def print_list(head:Node) -> None:
#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next:
#             print("-->",end=" ")
#         curr = curr.next
#     print()


# def partitioning(head:Node,x:int) -> Node:
#     left_dummy = Node()
#     right_dummy = Node()

#     left,right  = left_dummy,right_dummy
#     curr = head
#     while curr:
#         if curr.data < x:
#             left.next = curr
#             left = left.next
#         else:
#             right.next = curr
#             right = right.next
#         curr = curr.next
#     right.next = None
#     left.next = right_dummy.next
#     return left_dummy.next


# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(4)
#     head.next.next = Node(3)
#     head.next.next.next = Node(2)
#     head.next.next.next.next = Node(5)
#     head.next.next.next.next.next = Node(2)

#     print_list(head=head)
#     x = 3

#     head = partitioning(head=head,x=x)
#     print_list(head=head)


"""
Q 21 : Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
"""

# class Node:
#     def __init__(self,data = 0):
#         self.data = data
#         self.next = None

# def reverse_second(head:Node,left:int,right:int) -> Node:

#     if head is None:
#         return head

#     dummy = Node()
#     dummy.next = head

#     prev = dummy

#     for _ in range(1,left):
#         prev = prev.next


#     curr = prev.next
#     next_node = None
#     for _ in range(right-left + 1):
#         temp = curr.next
#         curr.next = next_node
#         next_node = curr
#         curr = temp

#     prev.next.next = curr
#     prev.next = next_node
#     return dummy.next

# def print_list(head:Node) ->None:
#     curr = head
#     while curr:
#         print(curr.data,end=" ")
#         if curr.next:
#             print("-->",end=" ")
#         curr = curr.next
#     print()


# if __name__ == "__main__":

#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)


#     print_list(head=head)
#     left = 2
#     right = 4
#     head = reverse_second(head=head,left=left,right=right)
#     print_list(head=head)


"""
22 Maximum Sum Subarray of Size K
"""


# def max_sub_arr(arr: list, k: int) -> int:
#     max_window = sum(arr[:k])
#     max_sum = max_window

#     for i in range(k, len(arr)):
#         print(i)
#         max_window += arr[i]
#         max_window -= arr[i - k]

#         max_sum = max(max_sum, max_window)
#     return max_sum


# if __name__ == "__main__":
#     arr = [2, 1, 5, 1, 3, 2]
#     k = 3

#     print("Max of sub arrays ", max_sub_arr(arr=arr, k=k))


"""
23 Given strings s and p, find all start indices of p's anagrams in s.
"""

# def anagrams(s:str,p:str):
#     p_len = len(p)
#     s_len = len(s)

#     p_count = {}
#     s_count = {}
#     res = []

#     for i in range(p_len):
#         p_count[p[i]] = p_count.get(p[i],0) + 1
#         s_count[s[i]] = s_count.get(s[i],0) + 1


#     if p_count == s_count:
#         res.append(0)


#     # sliding window
#     for i in range(p_len,s_len):
#         char_in = s[i]
#         s_count[char_in] = s_count.get(char_in,0) + 1

#         # print("S count ",s_count)
#         char_out = s[i - p_len]
#         s_count[char_out] -= 1


#         if s_count[char_out] == 0:
#             del s_count[char_out]


#         if s_count == p_count:
#             res.append(i - p_len + 1)

#     print("Result ",res)


# if __name__ == "__main__":
#     s = "cbaebabacd"
#     p = "abc"
#     anagrams(s=s,p=p)


"""
24 Permutation in String (LeetCode 567)

Problem: Given two strings s1 and s2, return true if s2 contains a permutation of s1.
"""

# def permuation(s1:str,s2:str) -> bool:
#     s1_len = len(s1)
#     s2_len = len(s2)
#     if s1_len > s2_len:
#         return False

#     s1_count = {}
#     s2_count = {}

#     for i in range(s1_len):

#         s1_count[s1[i]] = s1_count.get(s1[i],0) + 1
#         s2_count[s2[i]] = s2_count.get(s2[i],0) + 1
#     if s1_count == s2_count:
#         return True

#     for i in range(s1_len,s2_len):

#         char_in = s2[i]
#         s2_count[char_in] = s2_count.get(char_in,0) + 1


#         char_out = s2[i - s1_len]
#         s2_count[char_out] -= 1

#         if s2_count[char_out] ==0:
#             del s2_count[char_out]


#         if s1_count == s2_count:
#             return True

#     return False


# if __name__ == "__main__":
#     s1 = "hello"
#     s2 = "ooolleoooleh"
#     print("Result ",permuation(s1=s1,s2=s2))


"""
25 Sliding Window Maximum (LeetCode 239)
"""
# from collections import deque
# def window_max(arr:list,k:int)->int:
#     dq = deque()
#     n  = len(arr)
#     res = []


#     for i in range(n):

#         while dq and arr[dq[-1]] < arr[i]:
#             dq.pop()

#         dq.append(i)
#     print("value of dq ",dq)
#     if dq[0] == i - k:
#         dq.popleft()

#     if i >= k - 1:
#         res.append(arr[dq[0]])
#     print("Value of result ",res)


# if __name__ == "__main__":
#     nums = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3

#     window_max(arr=nums,k=k)


"""
26. Longest Substring Without Repeating Characters (LeetCode 3)
"""

# def logest_unique_substring(s:str) -> int:
#     char_set = set()

#     left = 0
#     max_length = 0

#     for right in range(len(s)):

#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1

#         char_set.add(s[right])


#         current_window_size = right - left + 1
#         max_length = max(max_length,current_window_size)

#     return max_length


# if __name__ == "__main__":
#     s = "abcabcbb"
#     print("Ans ",logest_unique_substring(s=s))
# requests = [
#     [1, 2, 10, 1],
#     [2, 3, 20, 2]
# ]

# inventory = 3

# from collections import deque, defaultdict

# def unallocated_users(requests,total_inventory):
#     allocated = defaultdict(int)
#     print("Allocated ",allocated)

#     requested = defaultdict(int)

#     for customer_id,qty,bid,time in requests:
#         requested[customer_id] += qty

#     requests.sort(key=lambda x: (-x[2],x[3],x[0]))

#     print("Sorted Reqeusts ",requests)

#     n = len(requests)

#     i = 0
#     while i < n and total_inventory > 0:
#         pass


# if __name__ == "__main__":
#     unallocated_users(requests=requests,total_inventory=inventory)


# def get_unallotted_users(requests, totalInventory):

#     # Track how much each customer received
#     allocated = defaultdict(int)

#     # Track original requested quantity
#     requested = defaultdict(int)

#     for customerId, qty, bid, timestamp in requests:
#         requested[customerId] += qty

#     # Sort:
#     # 1. Higher bid first
#     # 2. Earlier timestamp first
#     # 3. Smaller customerId first (stable tie breaker)
#     requests.sort(key=lambda x: (-x[2], x[3], x[0]))

#     n = len(requests)
#     i = 0

#     while i < n and totalInventory > 0:

#         current_bid = requests[i][2]

#         # Collect all customers with same bid
#         same_bid_group = []

#         while i < n and requests[i][2] == current_bid:

#             customerId, qty, bid, timestamp = requests[i]

#             # Ignore invalid qty
#             if qty > 0:
#                 same_bid_group.append(
#                     [customerId, qty]
#                 )

#             i += 1

#         # If no customers in this group
#         if not same_bid_group:
#             continue

#         # Total qty needed by this bid group
#         total_needed = sum(qty for _, qty in same_bid_group)

#         # --------------------------------------------------
#         # CASE 1:
#         # Enough inventory for whole group
#         # --------------------------------------------------
#         if totalInventory >= total_needed:

#             for customerId, qty in same_bid_group:
#                 allocated[customerId] += qty
#                 totalInventory -= qty

#         # --------------------------------------------------
#         # CASE 2:
#         # Not enough inventory -> round robin
#         # --------------------------------------------------
#         else:

#             q = deque(same_bid_group)

#             while q and totalInventory > 0:

#                 customerId, qty = q.popleft()

#                 # Allocate 1 item
#                 allocated[customerId] += 1
#                 qty -= 1
#                 totalInventory -= 1

#                 # Put back if still needs inventory
#                 if qty > 0:
#                     q.append([customerId, qty])

#     # ------------------------------------------------------
#     # RETURN USERS WHO GOT NOTHING
#     # ------------------------------------------------------
#     result = []

#     for customerId in requested:

#         if allocated[customerId] == 0:
#             result.append(customerId)

#     return sorted(result)


"""
27 : Paranthesis
n = 3
op = ["((()))","()()()","(())()"]
n = 1
op = ["()"]
"""

# def generate(n, curr="", open_count=0, close_count=0,result = None):
#     if result is None:
#         result = []

#     if len(curr) == 2 * n:
#         result.append(curr)
#         return result

#     if open_count < n:
#         generate(n, curr + "(", open_count + 1, close_count,result)

#     if close_count < open_count:
#         generate(n, curr + ")", open_count, close_count + 1,result)


#     print("length of result ",len(result))
#     return result


# if __name__ == "__main__":

#     n = 3
#     result = generate(n)
#     print("Result ",result)


# def find_error_nums(arr:list[int])->None:
#     error_num = 0
#     actual_num = 0
#     for i in range(len(arr)):
#         print("Number ",arr[i])
#         print("Compare Number ",i + 1)
#         if arr[i] != i+1:
#             error_num = arr[i]
#             actual_num = i + 1
#     print("Error Num ",error_num)
#     print("Actual Num ",actual_num)


# if __name__ == "__main__":
#     arr = [1,1]
#     find_error_nums(arr=arr)


"""
28 Build an Array With Stack Operations
"""


# class MyStack:
#     def __init__(self, capacity):

#         self.arr = [0] * capacity

#         self.capacity = capacity

#         self.top = -1

#     def push(self, data):
#         if self.top == self.capacity - 1:
#             print("You can`t add more element than that")
#             return
#         self.top += 1
#         self.arr[self.top] = data

#     def pop(self):
#         if self.top == -1:
#             print("Stack is empty")
#             return
#         value = self.arr[self.top]
#         self.top -= 1
#         return value

#     def is_empty(self):
#         return self.top == -1
    
    
#     def get_top(self):
#         return self.arr[self.top]


# def build_array_with_stack(arr: list[int], n: int) -> list[str]:
#     last_element = arr[len(arr) - 1]
#     st = MyStack(last_element)
#     res = []
#     for i in range(1,last_element + 1):
#         st.push(i)
#         res.append("Push")
#         if st.get_top() != arr[st.top]:
#             st.pop()
#             res.append("Pop")
    
#     print("Result ",res)
        
            


# if __name__ == "__main__":
#     arr = [1,2]
#     n = 3
#     build_array_with_stack(arr=arr,n=n)
#     pass


'''
29 You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
'''


# import operator

# def trunc_div(a,b):
#     return int(a / b)
 
# def eval_rpn(arr:list[str]) -> int:
#     operators = {
#         "+":operator.add,
#         "-":operator.sub,
#         "*":operator.mul,
#         "/":trunc_div
#     }    
#     s = MyStack(len(arr))
#     for elem in arr:
#         if elem.lstrip("-").isdigit():
#             s.push(int(elem))
#         else:
#             right = s.pop()
#             left = s.pop()           
#             result = operators[elem](left,right)
#             print("Result ",result)
#             s.push(result)
#     print("Stack ",s.get_top())
                

# if __name__ == "__main__":
#     arr = ["4","13","5","/","+"] #["10","6","9","3","+","-11","*","/","*","17","+","5","+"] #["4","13","5","/","+"]
#     eval_rpn(arr=arr)



'''
30. Delete the Middle Node of a Linked List
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Input: head = [1,2,3,4]
Output: [1,2,4]
'''
# import math
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None



# def print_list(head:Node) -> None:
#     current = head
#     while current:
#         print(current.data,end=" ")
#         current = current.next
    

# def delete_middle_node(head:Node) -> Node:
#     current = head
#     count = 0
#     while current:
#         current = current.next
#         count += 1
    
#     middle = math.ceil(count / 2)
#     print("Middle ",middle) 
    
#     i = 0
#     current = head
#     prev = current
#     while i < middle :
#         prev = current
#         current = current.next
#         i += 1
        
#     prev.next = current.next
#     return head



# if __name__ == "__main__":
#     # [1,3,4,7,1,2,6], [1,3]
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
    
#     print_list(head=head)
#     head = delete_middle_node(head=head)
#     print()
#     print_list(head=head)



'''
31 Substring with Concatenation of All Words
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''



# Naive approach using permtaion
# def substring_indexes(st:str,words:list[str]) -> list[int]:
#     result = []
    
    
#     def backtracking(path,used):
        
#         if len(path) == len(words):
#             result.append("".join(path))
#             return
        
        
#         for i in range(len(words)):
            
#             if used[i]:
#                 continue
            
#             path.append(words[i])
#             used[i] = True
            
            
            
#             backtracking(path,used)
            
            
#             path.pop()
#             used[i] = False
        
    
    
#     used = [False] * len(words)
#     backtracking([],used)
    
#     for word in result:
        
#         for i in range(len(st)):
            
#             chars = ""
#             for j in range(i,len(st)):
#                 chars += st[j]
#                 if chars == word:
#                     print("indexes ",i)


# Efficient approach using hashmap and sliding window 
def substring_indexes(st:str,words:list[str]) -> list[int]:
    indexes = []
    hash_map = {}
    word_len = len(words[0])
    window_size = sum(len(word) for word in words)
    
    
    # Create hashmap with words
    
    for word in words:
        if word in hash_map:
            hash_map[word] += 1
        else:
            hash_map[word] = 1
            
    
    
    # Window Sliding
    for i in range(len(st) - window_size + 1):
        window = st[i : i + window_size]
        chunks  = []
        for j in range(0,len(window),word_len):
            chunks.append(window[j:j + word_len])
        temp_map = {}
        for chunk in chunks:
            temp_map[chunk] = temp_map.get(chunk,0) + 1
        if temp_map == hash_map:
            indexes.append(i)
    print("Indexes ",indexes)
if __name__ == "__main__":
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    
    substring_indexes(st=s,words=words)