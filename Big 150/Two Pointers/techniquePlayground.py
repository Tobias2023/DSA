'''
Left and Right Boundary
Template

Another common usage is putting pointers on the left-most side and right-most side. One pointer starts from the beginning, while the other pointer starts from the end. They move toward each other until they meet in the middle.


The resulting algorithm is simple:

Set two pointers, one at each end of the input string
If the input is palindromic, both the pointers should point to equivalent characters, at all times. [1]
If this condition is not met at any point of time, we break and return early. [2]
We can simply ignore non-alphanumeric characters by continuing to traverse further.
Continue traversing inwards until the pointers meet in the middle.


Complexity Analysis

Time complexity : O(n)O(n), in length nn of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.

Space complexity : O(1)O(1). No extra space required, at all.
'''


# Test: Create a function printing each value on the left-most & right-most


def lr_boundary(arr):
  # Return is array is empty
 if len(arr) == 0:
   return False

  

  # while L index is 




# lr_boundary(["L","L","l","M","M","r","R","R"])
# ============| 0   1   2   3   4   5   6   7  |======= Index visibility ======