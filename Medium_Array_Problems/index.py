'''
Q1 : Next Permuation
nput: arr[] = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next lexicographically greater arrangement of the elements in the array arr[] is [2, 4, 5, 0, 1, 7].

Input: arr[] = [3, 2, 1]
Output: [1, 2, 3]
Explanation: This is the last permutation, so we return the lowest possible permutation (ascending order).

Input: arr[] = [1, 3, 5, 4, 2]
Output: [1, 4, 2, 3, 5]
Explanation: The next lexicographically greater arrangement of the elements in the array arr[] is [1, 4, 2, 3, 5].
'''

# +++++++++++++++++++++++++++++++++++++ Better approach using traversing from right to left 
def next_permuation(arr:list[int]) -> list[int]:
    n = len(arr)
    
    
    # step 1 find the breaking point traversing from right to left
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    
    # step 2 
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j  -= 1
        arr[i],arr[j] = arr[j],arr[i]
    
    
    left = i + 1
    right = n - 1
    
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        
        left += 1
        right -= 1
    
    
    return arr



if __name__ == "__main__":
    arr = [1, 3, 5, 4, 2]
    print("New Array ",next_permuation(arr=arr))
