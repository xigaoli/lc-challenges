
def binarySearch(arr, lo, hi, target): 
  
    while lo <= hi: 
  
        mid = lo + (hi - lo) // 2
        if arr[mid] == target: 
            return mid 
        elif arr[mid] < target: 
            lo = mid + 1
        else: 
            hi = mid - 1
    # If we reach here, then the element 
    # was not present 
    return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)
print(result)