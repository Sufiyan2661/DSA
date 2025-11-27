# Maximum Product of the triplet (Subsequence of the 3) in an array

# 1) Naive Approach

def maxProduct(arr):
    n = len(arr)
    maxProduct = -10**9
    
    for i  in range(n -2):
        for j in range(i + 1,n-1):
            for k in range(j + 1,n):
                maxProduct = max(maxProduct, arr[i] * arr[j] * arr[k])
    
    return maxProduct
    
    


arr = [10, 3, 5, 6, 20]
print(maxProduct(arr))