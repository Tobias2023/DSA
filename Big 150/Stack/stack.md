# How-to Guide/Resources 

* [How to guide](https://www.freecodecamp.org/news/data-structures-101-stacks-696b3282980/?msclkid=07534d4fc5ae11ec916aa44423721a92)

![Stack DSA](https://cdn-images-1.medium.com/max/1200/1*4Pn00ch_p4DTCb4r3naCDQ.png)

## Example blueprint:

```
# LIFO

class Stack: 
  def __init__(self, arr):
    self.arr = arr

  def length(self): # o(n)
    count = 0
    for i in self.arr:
      count+=1
    print(count)

  def add_item(self, item):
    self.arr.append(item)
    print(self.arr)
  

  def remove_item(self):
    if len(self.arr) == 0:
      return
    self.arr.pop()
    print(self.arr)

  



myStack = Stack([]) # Empty to see how items are being added

# myStack.length()
myStack.add_item(1)
myStack.add_item(2)
myStack.add_item(3)
myStack.add_item(3)
myStack.add_item(3)
myStack.add_item(3)
myStack.add_item(3)
myStack.remove_item()
myStack.remove_item()
myStack.remove_item()
myStack.remove_item()
myStack.remove_item()
myStack.remove_item()
myStack.remove_item()
myStack.remove_item()
myStack.remove_item()



```