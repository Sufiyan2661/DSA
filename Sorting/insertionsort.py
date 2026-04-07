def insertion_sort(arr):
    
    for i,j in enumerate(arr):
        
        key = arr[i+1]
        k=i-1
        breakpoint()
        while(k>=0 and key<arr[k]):
            arr[k+1] = arr[k]
            k-=1
            breakpoint()
            
        arr[k+1] = key
        breakpoint()
        
    return arr


arr = [12,11,13,5,6]
print(insertion_sort(arr))