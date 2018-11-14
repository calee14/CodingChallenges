'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
# My answer
import time
def foo():
    print('Hello World')
def solution(f, n):
    time.sleep(n/1000)
    f()
solution(foo, 1000)