## Binary Search

### Explanation 

> Binray search is a algorithm that takes a **sorted** structure and splits the structue until the value is found.

### Analogy

* If a person had a Phone book sorted for a-z, and they needed to locate a contact they would more than likely:
  * Split the book in half
  * Check the current page to see if they need to continue turning the page OR go back a few pages.

This set of instruction is Binary Search: 

### Template

```python
# Problem: Find the target (tar) in the array(arr) 

  def binary_search(arr, tar):
    left = 0 
    right = len(arr) - 1

  while right > left: 
    mid = right-left // 2 
    if arr[mid] == tar: 
      return f"{arr[mid]} found at {[mid]}"
    if arr[mid] > tar: 
      right = mid - 1
    if arr[mid] < tar:
      left = mid + 1 

# Testcases:

print(binary_search([1,2,3,4,5,6,7,8,], 7))

```