# 1 => Quick sorting using first element as the pivot element
# def quick_sort(arr,low,high):
#     if low < high:
#         pivot = arr[low]
#         k = high
#         i  = high
#         while i > low:
#             if arr[i] > pivot:
#                 arr[i],arr[k] = arr[k],arr[i]
#                 k = k - 1

#             i = i - 1
#         arr[k],arr[low] = arr[low],arr[k]
#         quick_sort(arr,low,k - 1)
#         quick_sort(arr,k + 1,high)
# if __name__ == "__main__":
#     arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]
#     low = 0
#     high = len(arr) - 1
#     print("Original Array ",arr)
#     quick_sort(arr,low,high)
#     print("After sorting ",arr)


# Quick sort using last element as the pivot
# def quick_sort(arr, low, high):
#     if low < high:
#         pivot = arr[high]
#         i = low 
#         k = low
#         while i < high:
#             if arr[i] < pivot:
#                 arr[i],arr[k] = arr[k],arr[i]
#                 k = k + 1
#             i = i + 1
#         arr[k],arr[high] = arr[high],arr[k]
#         quick_sort(arr,low,k - 1)
#         quick_sort(arr,k + 1,high)


# if __name__ == "__main__":
#     arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]
#     low = 0
#     high = len(arr) - 1 
#     print("Original Array ",arr,"\n")
#     quick_sort(arr,low,high)
#     print("Sorted Array ",arr)



# => Quick sorting by taking random element as a pivot by using hoare`s algorithm
# import random

# def partition(arr,low,high):
#     pivot = arr[low]
#     i = low - 1
#     j = high + 1
    
#     while True:
        
        
#         # Move to the right
#         while True:
#             i = i + 1
#             if arr[i] >= pivot:
#                 break
#         # Move to the left
#         while True:
#             j = j - 1
#             if arr[j] <= pivot:
#                 break
        
#         if i >= j:
#             return j
        
#         arr[i], arr[j] = arr[j],arr[i]


# def partition_r(arr,low,high):
#     r = random.randint(low,high)
#     arr[r],arr[low] = arr[low],arr[r]
#     return partition(arr,low,high)


# def quick_sort(arr,low,high):
#     if low < high:
#         p = partition_r(arr,low,high)
#         quick_sort(arr,low,p)
#         quick_sort(arr,p + 1,high)


# if __name__ == "__main__":
#     arr = [2,34,503,392,3,21,23,45,5]
#     low = 0
#     high = len(arr) - 1
#     print("Original array ",arr)
#     quick_sort(arr,low,high)
#     print("sorted array ",arr)
    