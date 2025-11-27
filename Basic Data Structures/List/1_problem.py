# Second Largest Element
# There are three approaches


# 1) Naive Approach


# def getSecondLargest(arr):
#     n = len(arr) # 5


#     # Here first sort in the ascending order (Non-Decreasing order)
#     arr.sort()


#     for i in range(n -2,-1,-1):
#         if arr[i] != arr[n-1]:
#             return arr[i]


# 2) Better Approach (Two Pass Search)


# def getSecondLargest(arr):
#     n = len(arr)

#     largest = -1
#     secondLargest = -1


#     # Finding the largest element
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]

#     # Finding the second largest
#     for i in range(n):
#         if arr[i] > secondLargest and arr[i] != largest:
#             secondLargest = arr[i]

#     return secondLargest


# 3) Expected Approach (one Pass Search)


# def getSecondLargest(arr):
#     n = len(arr)
#     largest = -1
#     secondLargest = -1
#     for i in range(n):

#         if arr[i] > largest:
#             secondLargest = largest
#             largest = arr[i]

#         elif arr[i] < largest and arr[i] > secondLargest:
#             secondLargest = arr[i]
#     return secondLargest


# if __name__ == "__main__":
#     arr = [12, 35, 1, 10, 34, 1]
#     print(getSecondLargest(arr))
