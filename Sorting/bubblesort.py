def bubble_sort(arr:list)->list:
    n = len(arr)
    
    breakpoint()
    for i in range(n):
        
        breakpoint()
        swapped = False
        
        for j in range(0,n - i - 1):
            breakpoint()
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                breakpoint()
                swapped = True
        
            breakpoint()
        
        breakpoint()
        if swapped == False:
            break


    return arr

if __name__ == "__main__":
    arr = [5,6,1,3]
    new_arr = bubble_sort(arr=arr)
    print("new array ",new_arr)