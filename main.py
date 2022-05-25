
def binary_search(arr, tar):
  left = 0 
  right = len(arr) - 1

  while right > left: 
    mid = right-left // 2 
    if arr[mid] == tar: 
      return f"{arr[mid]} found at Index: {[mid]}"
    if arr[mid] > tar: 
      right = mid - 1
    if arr[mid] < tar:
      left = mid + 1 

# Testcases:

print(binary_search([1,2,3,4,5,6,7,8,], 7))