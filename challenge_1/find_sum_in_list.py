'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
import time

numbers = [10, 15, 3, 7]
# O(N^2)
def find_sum(nums, k):
  for num in nums:
    for num1 in nums:
      if num + num1 == k:
        return [num, num1]
  return [0]

start_time_1 = time.time()
result_1 = find_sum(numbers, 17)
end_time_1 = time.time() - start_time_1
print(end_time_1, "s")
print(result_1)

# My improved version
# Not completed
# def find_sum_(nums, k):
#   for i in range(len(nums)):
#     target = k-nums[i]
#     while True:

start_time_2 = time.time()
result_2 = find_sum_(numbers, 17)
end_time_2 = time.time() - start_time_2
print(end_time_2, "s")
print(result_2)

if end_time_1 > end_time_2:
  print('Mine is faster')
else:
  print('O(N^2) is faster')

# Answer
def find_sum_(list_nums, target):
  '''
  Use a hash set to store the number we have seen. Then whenever we see a new
  number, check whether the difference of it and the target already in the
  hash set.
  Args:
      list_nums(list): a list of number
      target(int): the sum that is looked for
  returns:
      bool: whether there is a pair of numbers add up to target
  '''
  num_seen_set = set()
  for num in list_nums:
    print(num_seen_set)
    print(target - num)
    if target - num in num_seen_set:
      return True
    else:
      num_seen_set.add(num)
  return False

start_time_3 = time.time()
result_3 = find_sum_(numbers, 17)
end_time_3 = time.time() - start_time_3
print(end_time_3, "s")
print(result_3)