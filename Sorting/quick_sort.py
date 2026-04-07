# Quick sorting using first element as the pivot element
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
