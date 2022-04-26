'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

------ INCOMPLETE ------- 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

example: 
['n','o','o','n']

'''

# https://afteracademy.com/blog/what-is-the-two-pointer-technique [Review]

def isPalindrome(s):
  # check if empty string
  if s == "":
    return -1 
  # create a new string variable with out sp chars 
  new_string  = "".join([i for i in s if i.isalnum()]).lower()
  # create two pointers L,R (Passing the len of the new_string var)
  l,r = 0, len(new_string) - 1
  # start while loop 
  while l < r:
    # return false if L,R pointers don't match 
    if new_string[l] != new_string[r]:
      return False
    l+=1
    r-=1
  return True
  



print(isPalindrome("Noon")) # True
print(isPalindrome("Bob")) # True
print(isPalindrome("ToBias!#4")) # False


# {COMPLETED} 

## ==================== LEETCODE =================================

'''
04/18/2022 11:15	Accepted	47 ms	14.6 MB	python3

Runtime: 47 ms, faster than 87.47% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.6 MB, less than 44.33% of Python3 online submissions for Valid Palindrome.


'''