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
