'''

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.


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

def firstPalindrome(words):
  # loop through the words
    for i in words:  
    # run function to check if pal return that value 
      if isPalindrome(i): 
        return i
        
    return ""


  
print(firstPalindrome(["abc","car","ada","racecar","cool"])) # "ada"
print(firstPalindrome(["notapalindrome","racecar"])) # "racecar"
print(firstPalindrome(["blahh","mkdalnd"])) # ""

'''

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

def firstPalindrome(words):
  # Check is words array is empty 
  if len(words) == []:
    return ""

  # loop through the words
    for i in range(len(words)):  
    # run function to check if pal return that value 
      if isPalindrome(words[i]): 
        return words[i]
  return ""




  