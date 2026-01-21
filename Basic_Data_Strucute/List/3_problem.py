# Maximum consecutive 1s and 0s in a binary array

# 1) Approach -1 (Using simple traversal)


# def maxConsecutiveBits(arr):
#     maxCount = 0
#     count = 1
#     n = len(arr)
    
    
#     for i in range(1,n):
#         if arr[i] == arr[i-1]:
#             count += 1
#         else:
#             maxCount = max(maxCount,count)
#             count = 1
    
#     return count

# 2) Approach -2 (Using Bit Manipulation)
# def maxConsecutiveBits(arr):
#     maxCount = 0
#     count = 0
#     prev =-1
    
#     for num in arr:
#         if (num ^ prev) == 0:
#             count += 1
#         else:
#             maxCount = max(maxCount,count)
#             count =1 
#         prev = num
    
#     return max(maxCount,count)
            


# if __name__ == "__main__":
#     arr = [0,1,0,1,1,1,1]
#     print(maxConsecutiveBits(arr))