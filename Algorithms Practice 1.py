#Algortihms
#
#Linear search takes n tries at worst case scenario to dinf the value
#so if the dataset is 100 then it would take 100 as a worse case scenario
#
#Binary search requires a sorted list
# Binary search will take O(log n) in the worst case cenario
#
#Merge sort has a Big O notation of O(n log n)
#

########## Linear Search#############
def linear_search(list, target):
  """
  returns the index position of the target if found, else returns None
  """

  for i in range(0, len(list)):
    if list[i] == target:
      return i 
  return None
  
  
  
def verify(index):
  if index is not None:
    print("Target is found at index: ", index)
  else:
      print("item not found")

numbers = [1,2,3,4,5,6,7,8,9,10]


result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
