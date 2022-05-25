# Hashing 101

[Explaination](https://www.freecodecamp.org/news/what-is-hashing/)

## How Hashing works in Python Lang:

```
   # Few languages like Python, Ruby come with an in-built hashing support.
   
   # Declaration
   
    my_hash_table = {}
    my_hash_table = dict()

   # Insertion
   
    my_hash_table[key] = value

   # Look up
   
    value = my_hash_table.get(key) # returns None if the key is not present || 
    Deferred in python 3, available in python 2
    
      value = my_hash_table[key] # throws a ValueError exception if the key is not present

    # Deletion
    
    del my_hash_table[key] # throws a ValueError exception if the key is not present

    # Getting all keys and values stored in the dictionary
    
    keys = my_hash_table.keys()
    values = my_hash_table.values()

```


## Implementation: 

```
'''
Hashing [Pop Quiz]: 

- Declaration +
- Insertion 
- Look up
- Deletion
- Get all keys

'''
# Declaration
# table1 = {}
# table2 = dict(one=1,two=2)
# print(f"First item [Completed]: \n {table1} \n {table2}") 

# # Insertion -> hashTable // "three": 3
# table1["three"] = 3 
# # print(f"Second item [Completed]: \n {table1} \n {table2}")

# # Look up -> Look up item two // 'two': 2
# print(table2.get("two"))
# print(table2["two"])

# # Deletion - > delete "three"
# table1.pop("three")
# print(table1)

# get all keys -> table2
# for key in table2: 
#   print(table2[key])
# ans = table2.values()
# print(sum(ans))

# Using a HashTable/ Dict Count char occurences

def countValues(strr):
  # lowercase the String chars
  s = strr.lower()
  # initialize table 
  table = {}
  # loop through string adding/ counting vars to the table
  for char in range(len(s)): 
    if(not table.get(s[char])):
      table[s[char]] = 1
    else:
      table[s[char]] = table[s[char]]+1
  return table

def getSum(tab): 
  r = tab.values()
  total = 0
  for i in r:
    total+=i
  
  return total

def deleteVal(tab, val): # What if it doesn't exsit?
  if(not tab.get(val)):
    return -1
  tab.pop(val)
  return tab
    


# print(countValues("ttttttBBb"))
# print(getSum({"One": 1, "Twenty": 20}))
print(deleteVal({"One": 1, "Twenty": 20}, "Twenty"))

```