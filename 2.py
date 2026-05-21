# Reverse an array in place

arr = [1, 4, 5, 6, 2, 0, 7]

def reversearry(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1
    
    return arr

result = reversearry(arr)
print(result)
