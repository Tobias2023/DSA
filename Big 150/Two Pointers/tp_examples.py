# Two Pointer examples: 


def side_side(arr):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      print ("Left: " , arr[i])
      print ("Right: " , arr[j])


# side_side([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def meet_in_middle(arr):
  l,r = 0 , len(arr) - 1

  while l <= r: 
    print(f"Left: {arr[l]} | Right: {arr[r]}")
    l+=1
    r-=1

# meet_in_middle([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

def middle_outwards(arr):
  mid = len(arr) // 2
  l,r = mid -1, mid 
  print(f"Left: {arr[l]} | Right: {arr[r]}")

