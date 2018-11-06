'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

# My Answer
array_ints = [3,4,-1,1] # given arrays
array_ints = [1,2,0]
array_ints = [0,1,2,32,45,6,7,5,3] # testing if function works
def find_lowest_missing_int(l):
  l.sort()
  smallest_num = 1
  for num in l:
    if num > 0 and smallest_num < num:
      pass
    elif num > 0 and smallest_num >= num:
      smallest_num += 1
  return smallest_num
result = find_lowest_missing_int(array_ints)
print(result)