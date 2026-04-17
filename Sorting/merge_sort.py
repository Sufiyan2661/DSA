# def merge(arr,left,mid,right):
#     n1 = mid - left + 1
#     n2 = right - mid


#     # create temp arrays
#     L = [0] * n1
#     R = [0] * n2

#     # store left side values
#     for i in range(n1):
#         L[i] = arr[left + i]
#     # store right side values
#     for j in range(n2):
#         R[j] = arr[mid + 1 + j]


#     i = 0
#     j = 0
#     k = left


#     # move the left side element to orginal arr if left side element is less then or equal to  right side
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

#     # move the remaining elements  of L if there are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1

#     # move the remaining elements of R if there are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1


# def merge_sort(arr,left,right):
#     if left < right:
#         mid = (left + right) // 2
#         merge_sort(arr,left,mid)
#         merge_sort(arr,mid + 1,right)
#         merge(arr,left,mid,right)


# if __name__ == "__main__":
#     arr = [32,45,8,1,66,82,2,4]
#     left = 0
#     right = len(arr) - 1
#     print("Original Array ",arr)
#     merge_sort(arr,left,right)

#     print("Sorted Array ",arr)


# def merge_sort(arr,left,right):
#     if left < right:
#         mid = (left + right) // 2
#         merge_sort(arr,left,mid)
#         merge_sort(arr,mid+1,right)


#         n1 = mid - left + 1
#         n2 = right - mid

#         L = [0] * n1
#         R = [0] * n2

#         for i in range(n1):
#             L[i] = arr[left + i]
#         for j in range(n2):
#             R[j] = arr[mid + 1 + j]


#         i = 0
#         j = 0
#         k = left

#         while i < n1 and j < n2:
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1

#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while i < n1:
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < n2:
#             arr[k] = R[j]
#             j += 1
#             k += 1

# if __name__ == "__main__":
#     arr = [32,45,8,1,66,82,2,4]
#     left = 0
#     right = len(arr) - 1
#     print("Original Array ",arr)
#     merge_sort(arr,left,right)

#     print("Sorted Array ",arr)