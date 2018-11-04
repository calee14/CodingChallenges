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
