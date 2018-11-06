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

# Correct Solution
'''
Some other thoughts:
A naive method to solve this problem is to search all positive integers, starting
from 1 in the given array. We may have to search at most n+1 numbers in the given
array. So this solution takes O(n^2) in worst case.
We can use sorting to solve it in lesser time complexity. We can sort the array
in O(nLogn) time. Once the array is sorted, then all we need to do is a linear
scan of the array. So this approach takes O(nLogn + n) time which is O(nLogn).
We can also use hashing. We can build a hash table of all positive elements in
the given array. Once the hash table is built. We can look in the hash table for
all positive integers, starting from 1. As soon as we find a number which is not
there in hash table, we return it. This approach may take O(n) time on average,
but it requires O(n) extra space.
'''

def solution(alist):
    '''
    Use the index of the list to denote whether we have seen this number.
    For example:
        We see 2, then change the number on index 2 from + to -.
        [2, 4, 1]  -->  [2, 4, -1]
    ------
    Args:
        alist(list): a list of numbers may includes duplicates and negative
    Returns:
        int: the smallest positive integer missing in the given list
    '''
    pos_list = remove_negative(alist)
    modify_index(pos_list)
    smallest_pos = find_smallest_pos(pos_list)
    return smallest_pos


def remove_negative(alist):
    '''
    Args:
        alist(list): a list of numbers may includes duplicates and negative
    Returns:
        list: a list of numbers may includes only duplicates, no negative and 0
    '''

    '''
    Note:
        When reading, 'alist' is a reference to the original 'list', and 'list[:]'
        shallow-copies the list.
        When assigning, 'alist' (re)binds the name and 'alist[:]' slice-assigns,
        replacing what was previously in the list.
    '''
    # filter seems not an in-place modification
    # new_list = list(filter(lambda x: x > 0, alist))

    # following is not an in-place way either
    # alist = [x for x in alist if x > 0]

    # finally, this seems like an in-place operate as the id(alist) remains same
    # correct me if I'm wrong
    alist[:] = [x for x in alist if x > 0]
    return alist


def modify_index(pos_list):
    '''
    Args:
        pos_list(list)
    Returns:
        list
    '''
    for num in pos_list:
        if abs(num) - 1 < len(pos_list) and pos_list[abs(num) - 1] > 0:
            pos_list[abs(num) - 1] = - pos_list[abs(num) - 1]


def find_smallest_pos(pos_list):
    # return pos_list
    '''
    Args:
        pos_list(list)
    Returns:
        int
    '''
    for idx, num in enumerate(pos_list):
        if num > 0:
            return idx + 1
    return len(pos_list) + 1


def main():
    # test_list = [3, 4, -1, 1]
    # test_list = [1, 2, 0]
    test_list = [2, 4, -8, 10, 15, 0, 0 , -1, 1]
    # test_list = [0, 0, 0]
    print solution(test_list)

if __name__ == '__main__':
    main()