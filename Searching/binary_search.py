
def binary_search(arr:list,target:int) -> int:
    
    
    left = 0
    right = len(arr) - 1
    while left <= right:
        
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            left = mid + 1
        
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    print("Answer ",binary_search(arr=arr,target=11))