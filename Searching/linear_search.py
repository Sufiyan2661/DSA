# Linear Search
'''
[1,3,2,4,9,7]
'''


def linear_search(arr:list,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    arr = [1,3,2,4,9,7]
    print("Answer ",linear_search(arr=arr,target=3))
    
