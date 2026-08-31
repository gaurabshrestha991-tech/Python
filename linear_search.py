#       Linear Search Using Recursion

def linear_search(arr, key, index):
    if index == len(arr):
        return -1
    
    if arr[index] == key:
        return index
    
    return linear_search(arr, key, index + 1)


arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

result = linear_search(arr, key, 0)

if result == -1:
    print("Element not found")
else:
    print("Element found at position", result + 1)
