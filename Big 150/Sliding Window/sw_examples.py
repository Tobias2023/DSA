'''
Overview:
  - I think of it as more a technique than an algorithm. It's a technique that could be utilized in various algorithms.

I think the technique is best understood with the following example. Imagine we have this array:

Problem:
[ 5, 7, 1, 4, 3, 6, 2, 9, 2 ]
How would we find the largest sum of five consecutive elements?   

Steps: 
  - Create a variable to track the largest sum 
  - Use two pointers:
    - First pointer; at zero index (step forward each iteration)
    - Minus that first index s

'''
# [4,9,5,2,6,3,9,9,1,2,3,8,7,2,6,2,3,9]

def s_w(arr):
  # variable to keep track of highest amount 
  height_amount = 0
  # variable for two pointer indices
  i,j = 0, i+5

  while j < len(arr) - 1:
    print(j)
    j+=1
    i+=1
  
  # return highest
s_w([4,9,5,2,6,3,9,9,1,2,3,8,7,2,6,2,3,9])


