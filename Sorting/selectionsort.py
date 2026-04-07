

def selection_sort(arr:list)->list:
    n = len(arr)
    
    for i in range(n):
        
        min_idx = i
        
        for j in range(i+1,n):
            
            if arr[j] < arr[min_idx]:
                
                
                min_idx = j
                
        
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    
    return arr


if __name__ == "__main__":
    arr = [64,25,12,22,11]
    print("New array ",selection_sort(arr=arr))