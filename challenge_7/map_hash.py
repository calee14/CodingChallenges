'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

# I couldn't solve this question because I didn't know how I would match the various combinations with the correlating map dictionary.

# Correct solution. Got this from github.
'''
Not sure if '10001' is valid;
Question: How do deal with 0 if there are any?
Let's just assume there is no ZERO in the message;
'''


def solution(message):
    '''
    To decode message.
    Args:
        message(string)
    Returns:
        int
    '''
    # return decode_cnt(list(message))
    return decode_cnt(list(message))


def decode_cnt_no_zero(msg_list):
    '''
    Args:
        msg_list(list)
    Returns:
        int
    '''
    # if the length of the message is less than or equal to one then return 1 to the total amount of combinations.
    if len(msg_list) <= 1:
        return 1
    # if the message has more than two digits
    if len(msg_list) >= 2:
    	# check if the substring of first two is less than 26
        if 1 <= int(''.join(msg_list[0:2])) <= 26:
        	# recursively check the amount of combinations there are in after the first digit and the second digit
            return  (decode_cnt_no_zero(msg_list[1:]) +
                        decode_cnt_no_zero(msg_list[2:]))
        # if the list doesn't contain a number that is less than 26 then there isn't an letter that corresponds to that number
        return decode_cnt_no_zero(msg_list[1:])

"""
def decode_cnt(msg_list):
    '''
    A solution trying to solve when there are zeros.
    Args:
        msg_list(list): the list of message waiting for decoding
    Returns:
        int: count of how many ways to decode
    '''
    if len(msg_list) == 1:
        return 1 if int(msg_list[0]) != 0 else 0
    if len(msg_list) == 2:
        count = 0
        if int(msg_list[0]) != 0 and int(msg_list[1]) != 0:
            count += 1
        if 1 <= int(''.join(msg_list)) <= 26:
            count += 1
        return count
    if len(msg_list) > 2:
        count = 0
        if int(msg_list[0]) != 0:
            count += decode_cnt(msg_list[1:])
        if 1 <= int(''.join(msg_list[0:2])) <= 26:
            count += decode_cnt(msg_list[2:])
        return count
"""

def main():
    msg = '1109'
    print(solution(msg))

if __name__ == '__main__':
    main()