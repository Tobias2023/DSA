'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Plan: 

 - Hash map 

'''
#[ 1,2,3,4,9,7]
#[ 1,2,3,4,5,6]

def isAnagram(s, t):
  # return false if length is not the same 
  if len(s) != len(t):
    return False
  # create to maps (for s and t)
  s_map, t_map = {}, {}
  # Loop through s,t adding arr value as key and , counter for map value
  for i in range(len(s)):
    s_map[s[i]] = 1 + s_map.get(s[i], 0)
    t_map[t[i]] = 1 + t_map.get(t[i], 0)
  # loop through both map to check in counter value is the same   
  for j in s_map: 
    if s_map[j] != t_map.get(j, 0): # gets the value in s_map, compares to t_map
      return False
  
  return True

print(isAnagram("car", "rat")) # false 
print(isAnagram("anagram", "agnarma")) # True

# ==================== Leetcode Submission  ======================================
# Approach: Hash map

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length of both strings are not correct return False
        if len(s) != len(t):
            return False
        
        # create to hash tables
        s_map,t_map = {}, {}
        
        # Add values to tables
        
        for i in range(len(s)): 
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        
        # return false if hash table counter values don't match
        for j in s_map: 
            if s_map[j] != t_map.get(j, 0): 
                return False
        return True
'''

# 04/12/2022 12:56	Accepted	97 ms	14.5 MB	python3
